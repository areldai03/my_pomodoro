import tkinter as tk
import tkinter.ttk as ttk
from pomodoro import PomodoroTimer
import threading
import time

timer = PomodoroTimer()


def create_ui(root):
    root.title("pomodoro_tracker")
    root.geometry("300x200")

    # control_btnのイベント
    def time_control_btn(btn):
        timer_status = timer.get_timer_status()
        if timer_status['timer_status']:
            timer.stop_timer()
        else:
            timer.start_timer()



    def update_label():
        timer_status = timer.get_timer_status()
        if timer_status["timer_status"]:
            current_track = timer_status["current_track"]
            current_time = timer_status["current_time"]
            control_button.config(text='stop')
            control_button.config(bg='pink')

            minutes = current_time // 60
            seconds = current_time % 60
            timer_counter.config(text=f'{minutes:02}:{seconds:02}')

            track_num.config(text=f'track: {current_track}')
        else:
            control_button.config(text='start')
            control_button.config(bg='#87ceeb')


    def reset_btn():
        timer.reset()
        timer.start_timer()
        update_label()
        timer.stop_timer()

    # トラック数
    track_num = tk.Label(text="track:0", bg='cyan1', relief=tk.RIDGE)
    track_num.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

    # タイマー
    timer_counter = tk.Label(text='00:00', bg='red', relief=tk.RIDGE, font=("Helvetica", 24))
    timer_counter.grid(row=1, column=0, padx=5)

    # タイマーコントロールボタン
    control_button = tk.Button(text="start", command=lambda: time_control_btn(control_button), bg='#87ceeb')
    control_button.grid(row=2, column=0, padx=110, pady=5, sticky='w')
    reset_button = tk.Button(text="reset", command=reset_btn)
    reset_button.grid(row=2, column=0, padx=(0, 110), pady=5, sticky='e')

    def work_combo(event):
        timer.set_work_time(int(work_combobox.get()))


    def break_combo(event):
        timer.set_break_time(int(break_combobox.get()))

    # 作業時間、休憩時間の設定
    work_module = ("1","20","25","30")
    break_module = ("3","5","7","10")
    work_combobox = ttk.Combobox(root, width=7, height=4, state='readonly', values=work_module)
    break_combobox = ttk.Combobox(root, width=7, height=4, state='readonly', values=break_module)
    work_combobox.set("作業用")
    break_combobox.set("休憩用")
    work_combobox.bind('<<ComboboxSelected>>', work_combo)
    break_combobox.bind('<<ComboboxSelected>>', break_combo)
    work_combobox.grid(row=3, column=0, padx=80, pady=5, sticky='w')
    break_combobox.grid(row=3, column=0, padx=(0, 80), pady=5, sticky='e')







    # ウィンドウの列の伸縮性を調整
    root.grid_columnconfigure(0, weight=1)

    root.resizable(False, False)

    # ラベル更新
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
