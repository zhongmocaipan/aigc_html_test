from midiutil import MIDIFile

# 创建一个 MIDI 文件
midi_file = MIDIFile(1)

# 设置乐器（笛子）
track = 0
channel = 0
time = 0
program = 74  # 笛子乐器编号

# 添加乐器
midi_file.addProgramChange(track, channel, time, program)

# 音符数据
notes = [60, 62, 64, 65, 67, 69, 71, 72]  # 这些是 C 大调音阶的音符

# 添加音符
duration = 1
for note in notes:
    midi_file.addNote(track, channel, note, time, duration, 100)
    time += 1

# 写入 MIDI 文件
with open("chinese_music.mid", "wb") as f:
    midi_file.writeFile(f)
