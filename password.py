password = 'a123456'
i = 3 
while i > 0:
	密碼 = input('請設定密碼:')
	if 密碼 == password:
		print('登入成功')
		break
	else:
		i = i-1 
		if i > 0:
			print('GG 只剩', i,'次機會!')
	

	