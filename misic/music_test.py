# from midiutil import MIDIFile

# # 创建一个 MIDI 文件
# midi_file = MIDIFile(5)  # 五个轨道分别对应笛子、古筝、古琴、琵琶、二胡

# # 设置乐器
# instruments = [74, 0, 24, 105, 41]  # 笛子、古筝、古琴、琵琶、二胡的乐器编号
# for i, instrument in enumerate(instruments):
#     midi_file.addProgramChange(i, 0, 0, instrument)

# # 定义每个乐器的旋律
# melodies = {
#     "笛子": [60, 62, 64, 67, 64, 62, 60, 62, 64, 67, 69, 67, 64, 62, 64],
#     "古筝": [64, 62, 60, 62, 64, 64, 64, 62, 62, 62, 64, 67, 64, 62, 60],
#     "古琴": [67, 69, 71, 74, 71, 69, 67, 69, 71, 74, 76, 74, 71, 69, 67],
#     "琵琶": [69, 71, 72, 74, 76, 77, 76, 74, 72, 71, 69, 67, 69, 71, 72],
#     "二胡": [72, 74, 76, 79, 76, 74, 72, 74, 76, 79, 81, 79, 76, 74, 72]
# }

# # 添加每个乐器的旋律
# for i, (instrument, melody) in enumerate(melodies.items()):
#     time = 0
#     duration = 1
#     for note in melody:
#         midi_file.addNote(i, 0, note, time, duration, 100)
#         # 添加额外的延音效果
#         midi_file.addNote(i, 0, note, time + 0.5, duration, 100)
#         time += 1
#         duration = 0.5 if time % 4 == 0 else 1

# # 写入 MIDI 文件
# with open("chinese_music_with_multiple_instruments.mid", "wb") as f:
#     midi_file.writeFile(f)
from midiutil import MIDIFile

# 创建一个 MIDI 文件
midi_file = MIDIFile(5)  # 五个轨道分别对应笛子、古筝、古琴、琵琶、二胡

# 设置乐器
instruments = [74, 0, 24, 105, 41]  # 笛子、古筝、古琴、琵琶、二胡的乐器编号
for i, instrument in enumerate(instruments):
    midi_file.addProgramChange(i, 0, 0, instrument)

# 定义每个乐器的旋律
melodies = {
    "笛子": [60, 62, 64, 65, 67, 69, 71, 72],
    "古筝": [67, 69, 71, 72, 71, 69, 67, 69],
    "古琴": [64, 62, 60, 59, 57, 55, 54, 52],
    "琵琶": [69, 67, 65, 64, 62, 60, 59, 57],
    "二胡": [72, 71, 69, 67, 65, 64, 62, 60]
}

# 添加每个乐器的旋律
for i, (instrument, melody) in enumerate(melodies.items()):
    time = 0
    duration = 1
    for note in melody:
        midi_file.addNote(i, 0, note, time, duration, 100)
        # 添加额外的延音效果
        midi_file.addNote(i, 0, note, time + 0.5, duration, 100)
        time += 1
        duration = 0.5 if time % 4 == 0 else 1

# 写入 MIDI 文件
with open("liangzhu.mid", "wb") as f:
    midi_file.writeFile(f)
