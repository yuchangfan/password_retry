# 密碼重試程式
# 最多輸入3次密碼

password = 'a123456'
remain = 3
while remain > 0:
	remain = remain - 1
	enter = input('請輸入密碼： ')
	if enter == password:
		print('登入成功！')
		break
	else:
		print('密碼錯誤')
		if remain > 0:
			print('還有',remain , '次機會！')
		else:
			print('洗洗睡吧！')



