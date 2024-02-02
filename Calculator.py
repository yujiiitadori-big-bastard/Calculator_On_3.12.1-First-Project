#Easiest Version Of The Code
_FirstNum = int(input('Enter First Number: \n'))
_SecondNum = int(input('Enter Second Number: \n'))
_Operator = str(input('Enter The Operator You Want To Use: \n'))
if (_Operator == ('+')):
    _Action = '+'
elif (_Operator == ('-')):
      _Action = '-'
if (_Operator == ('*')):
    _Action = '*'
elif (_Operator == ('/')):
      _Action = '/'
else:
    work = str(('none'))
if (_Action == '+'):
     _Ans = (_FirstNum + _SecondNum)
     _Ans = str(_Ans) + ('.')
     print('The Sum Of', _FirstNum, 'And', _SecondNum, 'Is', _Ans)   
elif (_Action == '-'):
     _Ans = (_FirstNum - _SecondNum)
     _Ans = str(_Ans) + ('.')
     print('The Subtraction Of', _FirstNum, 'And', _SecondNum, 'Gives', _Ans)
if (_Action == '*'):
     _Ans = (_FirstNum * _SecondNum)
     _Ans = str(_Ans) + ('.')
     print('The Mutiplication Of', _FirstNum, 'And', _SecondNum, 'Gives', _Ans)   
elif (_Action == '/'):
     _Ans = (_FirstNum / _SecondNum)
     _Ans = str(_Ans) + ('.')
     print('The Division Of', _FirstNum, 'And', _SecondNum, 'Gives', _Ans)
else:
     _Work = ('0')
