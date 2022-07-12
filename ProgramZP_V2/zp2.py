print("\n ПРОГРАММА ОБРАБОТКИ ЗАРПЛАТЫ")


# Исполняющие функции
def readFile():
	file = open('register.txt', 'r')
	f = []

	for line in file:
		#print( line)
		line = line.split('-')
		#print(line)
		f.append(line[2])

	l2 = int(float(str(f[1])))
	l3 = int(float(str(f[2])))
	l4 = int(float(str(f[3])))
	l5 = int(float(str(f[4])))
	l6 = int(float(str(f[5])))
	l7 = int(float(str(f[6])))
	l9 = int(float(str(f[8])))
	l10 = int(float(str(f[9])))
	l11 = int(float(str(f[10])))
	l12 = int(float(str(f[11])))
	l13 = int(float(str(f[12])))
	l14 = int(float(str(f[13])))
	
	file.close()

	return l2, l3, l4, l5, l6, l7, l9, l10, l11, l12, l13, l14

def editFile(p='all', stag=0, smen=0, kas=0, kasW=0, anym=0, aqua=0):
	file = open('register.txt', 'r')
	f = []
	
	for line in file:
		f.append(line)
	file.close()
	
	if p!='all':
		file = open('register.txt', 'w')
	
	if p=='Dima':
		saveF = f[7:14]

		file.write("1-Работник-Дима-\n2-Стаж(шт)-{0}-\n3-Смены(шт)-{1}-\n4-Касса(грн)-{2}-\n5-КассаВыходной(грн)-{3}-\n6-Аниматор(ч)-{4}-\n7-Аквагрим(шт)-{5}-\n{6}{7}{8}{9}{10}{11}{12}".format(stag, smen, kas, kasW, anym, aqua, saveF[0], saveF[1], saveF[2], saveF[3], saveF[4], saveF[5], saveF[6]))

	elif p=='Katya':
		saveF = f[0:7]

		file.write("{0}{1}{2}{3}{4}{5}{6}8-Работник-Катя-\n9-Стаж(шт)-{7}-\n10-Смены(шт)-{8}-\n11-Касса(грн)-{9}-\n12-КассаВыходной(грн)-{10}-\n13-Аниматор(ч)-{11}-\n14-Аквагрим(шт)-{12}-".format(saveF[0], saveF[1], saveF[2], saveF[3], saveF[4], saveF[5], saveF[6], stag, smen, kas, kasW, anym, aqua))
	
	elif p=='all':
		editFile('Dima', stag, smen, kas, kasW, anym, aqua)
		editFile('Katya', stag, smen, kas, kasW, anym, aqua)
	
	if p!='all':
		file.close()

def addBazData():
	file = open('bazData.txt', 'a')
	L2, L3, L4, L5, L6, L7, L9, L10, L11, L12, L13, L14 = readFile()
	
	from time import gmtime, strftime
	
	data = strftime("%d:%m:%y", gmtime())
	
	file.write("Дата: {0}\n--------------------\n1-Работник-Дима-\n2-Стаж(шт)-{1}-\n3-Смены(шт)-{2}-\n4-Касса(грн)-{3}-\n5-КассаВыходной(грн)-{4}-\n6-Аниматор(ч)-{5}-\n7-Аквагрим(шт)-{6}-\n8-Работник-Катя-\n9-Стаж(шт)-{7}-\n10-Смены(шт)-{8}-\n11-Касса(грн)-{9}-\n14-КассаВыходной(грн)-{10}-\n15-Аниматор(ч)-{11}-\n16-Аквагрим(шт)-{12}-\n--------------------\n\n".format(data, L2, L3, L4, L5, L6, L7, L9, L10, L11, L12, L13, L14))
	file.close()
	
	print("\n Данные сохранены")

def editZP(p):
	addBazData()
	
	if p=='1':
		person = 'Dima'
		editFile(person)

	elif p=='2':
		person = 'Katya'
		editFile(person)

	elif p=='3':
		editFile()


# Основные функции
def balance():
	L2, L3, L4, L5, L6, L7, L9, L10, L11, L12, L13, L14 = readFile()

	moneyDima = (300*L2) + (400*(L3)) + (0.03*L4) + (0.015*L5) + (300*L6) + (35*L7)
	moneyKatya = (300*L9) + (400*(L10)) + (0.03*L11) + (0.015*L12) + (300*L13) + (35*L14)

	print("\n Баланс\n -------------\n Дима: {0}\n Катя: {1}\n -------------\n".format(moneyDima, moneyKatya))

def editDataDima():
	i = True
	while i==True:
		L2, L3, L4, L5, L6, L7, L9, L10, L11, L12, L13, L14 = readFile()
		print("\n Данные - Дима\n -------------------------\n Записаные данные:\n\n Дни стажировки: {0}\n Cмены: {1}\n Будничная касса: {2}\n Выходная касса: {3}\n Аниматор: {4}\n Аквагрим: {5}\n -------------------------\n\n Изменить?\n".format(L2, L3, L4, L5, L6, L7))
		userInput = input(" Введенно: ")
		if userInput=='-':
			i = False
		elif userInput=='+':  
			print(" _______________________________\n\n Нужно добавить к...")
			person = 'Dima'
			stag = int(input(" Стажу: "))
			smena = int(input(" Сменам: "))
			kassa = int(input(" Кассе: "))
			kassaW = int(input(" Выходной кассе: "))
			anymator = int(input(" Аниматорству: "))
			aquagrim = int(input(" Аквагримам: "))
			stag += L2
			smena += L3
			kassa += L4
			kassaW += L5
			anymator += L6
			aquagrim += L7
			
			editFile(person, stag, smena, kassa, kassaW, anymator, aquagrim)
			
			print(" _______________________________")

def editDataKatya():
	i = True
	while i==True:
		L2, L3, L4, L5, L6, L7, L9, L10, L11, L12, L13, L14 = readFile()
		print("\n Данные - Катя\n -------------------------\n Записаные данные:\n\n Дни стажировки: {0}\n Cмены: {1}\n Будничная касса: {2}\n Выходная касса: {3}\n Аниматор: {4}\n Аквагрим: {5}\n -------------------------\n\n Изменить?\n".format(L9, L10, L11, L12, L13, L14))
		userInput = input(" Введенно: ")
		if userInput=='-':
			i = False
		elif userInput=='+':  
			print(" _______________________________\n\n Нужно добавить к...")
			person = 'Katya'
			stag = int(input(" Стажу: "))
			smena = int(input(" Сменам: "))
			kassa = int(input(" Кассе: "))
			kassaW = int(input(" Выходной кассе: "))
			anymator = int(input(" Аниматорству: "))
			aquagrim = int(input(" Аквагримам: "))
			stag += L9
			smena += L10
			kassa += L11
			kassaW += L12
			anymator += L13
			aquagrim += L14
			
			editFile(person, stag, smena, kassa, kassaW, anymator, aquagrim)
			
			print(" _______________________________")

def printDataAll(): 
	file = open('register.txt', 'r')
	f=[]

	for line in file:
		line = line.split("-")
		line = "{0} {1} {2} {3}".format(line[0], line[1], line[2], line[3])
		f.append(line)

	print("\n Все данные:\n -----------------------\n {0} {1} {2} {3} {4} {5} {6}\n {7} {8} {9} {10} {11} {12} {13}\n -----------------------".format(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9], f[10], f[11], f[12], f[13]))

	file.close()

def zp(): # Подблок отвечающий за сохранение, и обнуление данных
	i = 1
	while i==True:
		print("\n Выдача зарплаты\n ---------------------\n Это действие нельзя будет отменить.\n ---------------------\n\n Продолжить?")
		userInput = input("\n Введенно: ")
		
		if userInput=='+':
			print("\n Выдача зарплаты\n ---------------------\n 1.Дима\n 2.Катя\n 3.Все\n\n")
			userInput = input(" Введено: ")
			
			if (userInput=='1' or userInput=='2' or userInput=='3'):
				editZP(userInput)

			else:
				print("Не коректный ввод")

		elif userInput=='-':
			i = 0

		else:
			print("Не коректный ввод")


# Главное меню
def start():
	print(" _______________________________\n\n 1. Вывести баланс\n 2. Данные - Дима\n 3. Данные - Катя\n 4. Вывести все данные\n 5. Получить зарплату\n\n 0. Выход из программы")
	inputUser = input("\n Введенно : ")

	if inputUser=='1':
		balance()
	elif inputUser=='2':
		editDataDima()
	elif inputUser=='3':
		editDataKatya()
	elif inputUser=='4':
		printDataAll()
	elif inputUser=='5':
		zp()

	if inputUser=='0':
		exit()


if __name__=="__main__":
	while True:
	start()