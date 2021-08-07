# 密碼重試程式
# '最多輸入3次密碼'
# 不對的話，印出'密碼錯誤！ 還有__次機會。'
# 對的話，印出'登入成功！'

password = 'a123456'
remain = 3
while reamain > 0:
	enter = input('請輸入密碼： ')
	if enter == password:
		print('登入成功！')
		break
	else:
		remain = remain - 1
		print('密碼錯誤！還有',remain , '次機會')
		if remain == 0:
			print('洗洗睡吧！')



