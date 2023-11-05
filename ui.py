import tkinter as tk

def create_ui(root):
    root.title("pomodoro_tracker")
    root.geometry("300x200")

    # トラック数
    track_num = tk.Label(text="トラック数:", bg='cyan1', relief=tk.RIDGE)
    track_num.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)

    # タイマー
    timer_counter = tk.Label(text='00:00', bg='red', relief=tk.RIDGE,font=("Helvetica", 24))
    timer_counter.grid(row=1, column=0, padx=5)

    #タイマーコントロールボタン
    control_button = tk.Button(text="start")
    control_button.grid(row=2, column=0, padx=110, pady=5, sticky='w')
    reset_button = tk.Button(text="reset")
    reset_button.grid(row=2, column=0, padx=(0,110), pady=5, sticky='e')


    # ウィンドウの列の伸縮性を調整
    root.grid_columnconfigure(0, weight=1)

    root.resizable(False, False)


