import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter.font import Font
import difflib

root = tk.Tk()
root.title("Diff the text")
root.style = ttk.Style()
root.style.theme_use('clam')

# def show_diff(seqm):
#     output = []
#     for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
#         if opcode == 'equal':
#             output.append(seqm.a[a0:a1])
#         elif opcode == 'insert':
#             output.append('(insert "{}")'.format(seqm.b[b0:b1], a0))
#         elif opcode == 'delete':
#             output.append('(delete "{}")'.format(seqm.a[a0:a1]))
#         elif opcode == 'replace':
#             output.append('(replace "{}" with "{}")'.format(seqm.a[a0:a1], seqm.b[b0:b1]))
#             # print('range {}..{} of a with {}..{} of b'.format(a0, a1, b0, b1))
#         else:
#             raise RuntimeError("unexpected opcode")
#     return ''.join(output)


def onclick():
	txt1 = my_text1.get("1.0","end")
	txt2 = my_text2.get("1.0","end")
	# sm = difflib.SequenceMatcher(None, txt1, txt2)
	# txt=show_diff(sm)
	# lv.set(txt)
	text1_lines=txt1.splitlines()
	text2_lines=txt2.splitlines()
	d = difflib.Differ()
	diff = d.compare(text1_lines, text2_lines)
	lv.set('\n'.join(diff))

# def onenter():
# 	print("You pressed enter !")
# - - - - - - - - - - - - - - - - - - - - -
# 1st entry frame
entry_frame1 = tk.Frame(root, bg='Cadetblue',
                             relief=tk.RAISED)
entry_frame1.grid(row=0, column=0, sticky=tk.E + tk.W + tk.N + tk.S)



text_label1 = tk.Label(entry_frame1,bg='Cadetblue',fg='light cyan',font=('sans-serif',10,"bold"), text="Text-1")
text_label1.grid(row=0)


xscrollbar = ttk.Scrollbar(entry_frame1, orient='horizontal')
xscrollbar.grid(row=2, column=0, sticky='ew')

yscrollbar = ttk.Scrollbar(entry_frame1)
yscrollbar.grid(row=1, column=1, sticky='ns')


my_text1 = tk.Text(entry_frame1,
					wrap='none',
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set,
                    height=8,
                    width=50,
                    bg='white smoke')
xscrollbar.config(command=my_text1.xview)
yscrollbar.config(command=my_text1.yview)
my_text1.grid(row=1)
my_text1.insert(tk.END, "this is not\nme")
# my_text.bind("<return>", onenter)



# - - - - - - - - - - - - - - - - - - - - -
# 2nd entry frame
entry_frame2 = tk.Frame(root,  bg='Cadetblue',
                             relief=tk.RAISED)
entry_frame2.grid(row=0, column=1, sticky=tk.E + tk.W + tk.N + tk.S)


text_label2 = tk.Label(entry_frame2,bg='Cadetblue',fg='light cyan',font=('sans-serif',10,"bold"), text="Text-2")
text_label2.grid(row=0)

xscrollbar = ttk.Scrollbar(entry_frame2, orient='horizontal')
xscrollbar.grid(row=2, column=0, sticky='ew')

yscrollbar = ttk.Scrollbar(entry_frame2)
yscrollbar.grid(row=1, column=1, sticky='ns')

my_text2 = tk.Text(entry_frame2,
					wrap='none',
                    xscrollcommand=xscrollbar.set,
                    yscrollcommand=yscrollbar.set,
                    height=8,
                    width=50,
					bg='white smoke')
xscrollbar.config(command=my_text2.xview)
yscrollbar.config(command=my_text2.yview)
my_text2.grid(row=1)
my_text2.insert(tk.END, "this is \nme")


entry_frame = tk.Frame(root, bg='Cadetblue', relief=tk.RAISED)
entry_frame.grid(row=1,columnspan=2, sticky="ew")
button = tk.Button(entry_frame,activebackground='white',activeforeground='#00654e',bg='#00654e',fg='white',font=('sans-serif',10,"bold"),text="Click ME !", command=onclick)
button.grid(row=0)

lv= tk.StringVar()
label = tk.Label(entry_frame, textvariable=lv, anchor="nw",justify=tk.LEFT, fg="white", bg="black",height=10,width=90)
label.grid(row=1,sticky='ewns')
lv.set("Hello \nthis is test did you\nknow that")



root.mainloop()
