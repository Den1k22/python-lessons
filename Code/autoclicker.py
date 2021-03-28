from pynput import mouse
import threading
import keyboard
import os
import time

ONE_CLICK = 1


class ThreadController:

    def __init__(self):
        self.work = True

    def is_working(self):
        return self.work

    def change_state(self, state):
        self.work = state


class Point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def get_x(self):
        return self._x

    @property
    def get_y(self):
        return self._y


class PointsStorage:

    def __init__(self):
        self._points = []

    def add_point(self, point):
        self._points.append(point)

    def remove_last_point(self):
        if self._points:
            self._points.pop()

    def remove_all_points(self):
        self._points = []

    def get_points(self):
        return tuple(self._points)


def on_add_point(mouse_controller, points_storage):
    pos = mouse_controller.position
    points_storage.add_point(Point(pos[0], pos[1]))


def on_remove_last_point(points_storage):
    points_storage.remove_last_point()


def remove_all_points(points_storage):
    points_storage.remove_all_points()


def save_points(points_storage):
    points_storage.save()


def click_all_points(thread_controller, mouse_controller, clicking_points, sleep_time):
    for point in clicking_points:
        if not thread_controller.is_working():
            break

        mouse_controller.position = (point.get_x, point.get_y)
        time.sleep(0.05)
        mouse_controller.click(mouse.Button.left, ONE_CLICK)
        time.sleep(sleep_time)


def start_autoclicker(thread_controller, mouse_controller, clicking_points):
    while True:
        if not thread_controller.is_working():
            break

        click_all_points(thread_controller, mouse_controller, clicking_points, 0.1)


def on_one_autoclick_run(thread_controller, mouse_controller, points_storage):
    print("on_one_autoclick_run")

    for th in threading.enumerate():
        if th.name == "auto_clicker_job":
            return

    thread_controller.change_state(True)
    seq_thread = threading.Thread(
        target=click_all_points,
        daemon=True,
        args=[thread_controller, mouse_controller, points_storage.get_points(), 0.15],
        name="auto_clicker_job")
    seq_thread.start()


def on_start_autoclicker(thread_controller, mouse_controller, points_storage):
    print("on_start_autoclicker")

    for th in threading.enumerate():
        if th.name == "auto_clicker_job":
            return

    thread_controller.change_state(True)
    seq_thread = threading.Thread(
        target=start_autoclicker,
        daemon=True,
        args=[thread_controller, mouse_controller, points_storage.get_points()],
        name="auto_clicker_job")
    seq_thread.start()


def on_stop_autoclicker(thread_controller):
    print("on_stop_autoclicker")
    thread_controller.change_state(False)


def on_save_points(points_storage, file_name="points.txt"):
    f = open(file_name, "w")

    for point in points_storage.get_points():
        string_to_save = str(point.get_x) + "," + str(point.get_y) + "\n"
        f.write(string_to_save)

    f.close()


def load_points(points_storage, file_name="points.txt"):
    if os.path.isfile(file_name):
        f = open(file_name, "r")
    else:
        return False

    text = f.readlines()
    f.close()

    new_points = []
    ok_status = True

    for line in text:
        line = line.replace("\n", "")
        line = line.replace(" ", "")
        if (line == "" or line.startswith("#")):
            continue

        raw_coordinates = line.split(",")
        if (len(raw_coordinates) != 2):
            ok_status = False
            break

        if (raw_coordinates[0].isnumeric() and raw_coordinates[1].isnumeric()):
            # TODO check that coordinates are in monitor's dimensions
            new_points.append(Point(int(raw_coordinates[0]), int(raw_coordinates[1])))
        else:
            ok_status = False
            break

    if (len(new_points) > 0 and ok_status):
        points_storage.remove_all_points()

        for new_point in new_points:
            points_storage.add_point(new_point)

        return True
    else:
        return False


def on_load_points(points_storage):
    if load_points(points_storage):
        print ("Points loaded successfully")
    else:
        print ("Points were not loaded")


# def multiply_points():
#     clicking_points = prepare_clicking_points()

#     array_of_clicking_points = []

#     for i in range (0,26):
#         for point in clicking_points:
#             array_of_clicking_points.append([point[0], point[1] + 25*i])

#     f = open("coordinates.txt", "w")

#     for point in array_of_clicking_points:
#         temp_str = str(point[0]) + "," + str(point[1]) + "\n"
#         f.write(temp_str)

#     f.close()


def main():
    mouse_controller = mouse.Controller()

    points_storage = PointsStorage()
            
    thread_controller = ThreadController()
        
    add_point_shortcut = "ctrl+alt+space"
    remove_last_point_shortcut = "ctrl+alt+z"
    remove_all_points_shortcut = "ctrl+alt+c"
    start_autoclicker_shortcut = "ctrl+alt+["
    stop_autoclicker_shortcut = "ctrl+alt+]"
    one_autoclick_run_shortcut = "ctrl+alt+'"
    save_points_shortcut = "ctrl+alt+s"
    load_points_shortcut = "ctrl+alt+l"
    exit_shortcut = "ctrl+alt+q"

    # multiply_lines_shortcut = "ctrl+alt+k"

    keyboard.add_hotkey(add_point_shortcut, on_add_point, args=[mouse_controller, points_storage])
    keyboard.add_hotkey(remove_last_point_shortcut, on_remove_last_point, args=[points_storage])
    keyboard.add_hotkey(remove_all_points_shortcut, remove_all_points, args=[points_storage])
    keyboard.add_hotkey(start_autoclicker_shortcut, on_start_autoclicker, args=[thread_controller, mouse_controller, points_storage])
    keyboard.add_hotkey(stop_autoclicker_shortcut, on_stop_autoclicker, args=[thread_controller])
    keyboard.add_hotkey(one_autoclick_run_shortcut, on_one_autoclick_run, args=[thread_controller, mouse_controller, points_storage])

    keyboard.add_hotkey(save_points_shortcut, on_save_points, args=[points_storage])
    keyboard.add_hotkey(load_points_shortcut, on_load_points, args=[points_storage])
    
    # keyboard.add_hotkey(multiply_lines_shortcut, multiply_points)


    print("Press ctrl+alt+q to stop.")
    keyboard.wait(exit_shortcut)

main()