#Importing bank for payment stuff.
from bank import *

print("*****WELCOME TO ONLINE SHOPPING CENTER*****")
print("Here is the list of shopping items, please enter the number of item to add it to your cart")
def line():
    print('---------------------------')
line()
item=('Plain NotePad-------$10', 'Styled NotePad-------$20', 'Crosscheck NotePad----$30', 'Lines NotePad---------40$')
for number,letter in enumerate(item):
	print(number,letter)
line()
total=0
cart=list()
while True:
	ask=input("Do you want to continue shopping: ")
	if ask == 'y':
		user=input("Enter an item to add to cart: ")
		quantity=input("Enter the quantity: ")
		if user == '0':
			total=total+10
		elif user =='1':
			total=total+20
		elif user== '2':
			total=total+30
		elif user=='3':
			total=total+40
		else:
			print("Enter Valid Input")
		grand_total=total*(int(quantity))
		data=item[int(user)]
		cart.append(data)
		print("Your cart contains : ",cart,"Your grand total is", grand_total)
		DEL=input("Do you want to delete items from cart? ")
		if DEL=='y':
			for number,letter in enumerate(cart):
				print(number,letter)
			ent=input("enter the item you want to delete: ")
			enti=int(ent)
			cart.pop(enti)
			print(cart)
			#except:
			#	print("Please enter Y to delete items from cart and N to continue shopping")

	else:
		line()
		if len(cart)>0:
			check=input("Do you want to see your cart and grang total?")
			if check=='y':
				print("Your cart contains : ",cart,"Your grand total is", grand_total, "$")
				print("Thank you for shopping")
				print("Proceeding to check out....")
				payment(grand_total)
			else:
				print("Thank you for shopping")
		else:
			print("Thank you for visiting our shop")
		line()
		break


		
#cart()