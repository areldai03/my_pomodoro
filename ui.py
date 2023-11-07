import tkinter as tk
from pomodoro import PomodoroTimer
import threading
import time

timer = PomodoroTimer()
def create_ui(root):
    root.title("pomodoro_tracker")
    root.geometry("300x200")

    #control_btnのイベント
    def time_control_btn(btn):
        timer_status = timer.get_timer_status()
        if timer_status['timer_status']:
            timer.stop_timer()
            control_button.config(text='start')
            control_button.config(bg='#87ceeb')
        else:
            timer.start_timer()
            control_button.config(text='stop')
            control_button.config(bg='pink')


    def update_label():
        timer_status = timer.get_timer_status()
        if timer_status["timer_status"]:
            current_track = timer_status["current_track"]
            current_time = timer_status["current_time"]

            minutes = current_time // 60
            seconds = current_time % 60
            timer_counter.config(text=f'{minutes:02}:{seconds:02}')

            track_num.config(text=f'track: {current_track}')

    # トラック数
    track_num = tk.Label(text="track:0", bg='cyan1', relief=tk.RIDGE)
    track_num.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

    # タイマー
    timer_counter = tk.Label(text='00:00', bg='red', relief=tk.RIDGE,font=("Helvetica", 24))
    timer_counter.grid(row=1, column=0, padx=5)

    #タイマーコントロールボタン
    control_button = tk.Button(text="start", command=lambda: time_control_btn(control_button), bg='#87ceeb')
    control_button.grid(row=2, column=0, padx=110, pady=5, sticky='w')
    reset_button = tk.Button(text="reset")
    reset_button.grid(row=2, column=0, padx=(0,110), pady=5, sticky='e')

    # ウィンドウの列の伸縮性を調整
    root.grid_columnconfigure(0, weight=1)

    root.resizable(False, False)

    #ラベル更新
    def monitor_timer_status():
        while True:
            update_label()
            time.sleep(0.3)

    monitor_thread = threading.Thread(target=monitor_timer_status)
    monitor_thread.daemon = True
    monitor_thread.start()

    timer_thread = threading.Thread(target=timer.timer)
    timer_thread.daemon = True
    timer_thread.start()

    def on_closing():
        root.quit()

    root.protocol("WM_DELETE_WINDOW", on_closing)


