
# 讀取檔案，把資料整理成列表
def read_file(filename):
	dlogs = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			dlogs.append(line.strip())
	return dlogs

# 轉換資料
def convert(dlogs):
	conversation = []
	#name = None
	for dlog in dlogs:
		if dlog == 'Allen' or 'Tom':
			name = dlog
			continue
		conversation.append(name + ': ' + dlog)
	return conversation
	
# 寫入檔案
def write(conversation, filename):
	with open(filename, 'w') as f:
		for conv in conversation:
			f.write(conv + '\n')

# 主程式
def main(inputname, outputname):
	dlogs = read_file(inputname)
	conversation = convert(dlogs)
	write(conversation, outputname)

main('input.txt', 'output.txt' )
# print(read_file('input.txt'))