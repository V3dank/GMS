import mysql.connector as sql
import pyttsx3

conn=sql.connect(host='localhost',user='root',passwd='Shrey@505',database='grocery_shop')
if conn.is_connected():
    c = conn.cursor()



print('grocery shop management system')
print('1.login')
print('2.exit')
choice=int(input('Enter your choice: \n'))
z = "Y"


if choice==1:
    user_name=input('enter your user name: \n')
    password=input('enter your password: \n')
    while z == "Y" or z == "y":
        if user_name=='Vedank' and password=='Vedank@505':
            print('connected successfully')
            engine = pyttsx3.init()
            engine.say("connected successfully")
            engine.runAndWait()
            print("========================================")
            print('grocery shop')
            print('1.customer details')
            print('2.product details')
            print('3.worker details')
            print('4.see all customer details')
            print('5.see all product details')
            print('6.see all worker details')
            print('7.see one customer details')
            print('8.see one product details')
            print('9.see one worker details')
            print('10.Stock')
            print('11.Update Stock')
            print('12.Stock Check')
            print('13.Exit')


            engine = pyttsx3.init()
            engine.say("Enter the choice")
            engine.runAndWait()
            choice=int(input('Enter the choice: \n'))
    
    
            if choice==1:
                print('******************************************')
                cust_name = input('enter your name: \n')
                phone_no = int(input('enter your phone number: \n'))
                cost = float(input('enter your cost: \n'))
                sql_insert = "insert into customer_details values('{}',{},{})".format(cust_name,phone_no,cost)
                c.execute(sql_insert)
                conn.commit()
                print('data is updated')
                print('******************************************')

            

            elif choice==2:
                print('******************************************')
                product_name=input('enter product name: \n')
                product_cost=float(input('enter the cost: \n'))
                sql_insert="insert into product_details values(""'"+(product_name)+"',"+str(product_cost)+")"
                c.execute(sql_insert)
                conn.commit()
                print('data is updated')
                print('******************************************')

            
        
            elif choice==3:
                print('******************************************')
                worker_name=input('enter your name: \n')
                worker_work=input('enter your work: \n')
                worker_age=int(input('enter your age: \n'))
                worker_salary=float(input('enter your salary: \n'))
                phone_no =int(input('enter your phone number: \n'))
                sql_insert="insert into worker_detail values(""'"+(worker_name)+"'," "'"+(worker_work)+"',"+str(worker_age) +","+str(worker_salary)+","+str(phone_no)+ ")"
                c.execute(sql_insert)
                conn.commit()
                print('data is updated')
                print('******************************************')
        
        
        
            elif choice==4:
                print('******************************************')
                t=conn.cursor()
                t.execute('select*from customer_details')
                record=t.fetchall()
                for i in record:
                    print(i)
                print('******************************************')
            


            elif choice==5:
                print('******************************************')
                t=conn.cursor()
                t.execute('select*from product_details')
                record=t.fetchall()
                for i in record:
                    print(i)
                print('******************************************')

            

            elif choice==6:
                print('******************************************')
                t=conn.cursor()
                t.execute('select*from worker_detail')
                record=t.fetchall()
                for i in record:
                    print(i)
                print('******************************************')


            elif choice==7:
                y = 0
                print('******************************************')
                a=input('enter your name: \n')
                t='select*from customer_details where Name=("{}")'.format(a)
                c.execute(t)
                v=c.fetchall()
                for i in v:
                    print(v)
                    y += 1
                if y == 0:
                    print("Not Found")
                print('******************************************')


   
                

            elif choice==8:
                y = 0
                print('******************************************')
                a=input('enter your product name: \n')
                t='select*from product_details where Name=("{}")'.format(a)
                c.execute(t)
                v=c.fetchall()
                for i in v:
                    print(v)
                    y += 1
                if y == 0:
                    print("Not Found")
                print('******************************************')


            elif choice==9:
                y = 0
                print('******************************************')
                a=input('enter your name: \n')
                t='select*from worker_detail where Name=("{}")'.format(a)
                c.execute(t)
                v=c.fetchall()
                for i in v:
                    print(v)
                    y += 1
                if y == 0:
                    print("Not Found")
                print('******************************************')
                



            elif choice == 10 :
                print('******************************************')
                t=conn.cursor()
                t.execute('select*from stock')
                record=t.fetchall()
                for i in record:
                    print(i)
                print('******************************************')




            elif choice == 11:
                print('******************************************')
                product_name = input('enter product name: \n')
                quantity = float(input('Enter no. of products: \n'))
                sql_insert="insert into stock values('{}',{})".format(product_name , quantity)
                c.execute(sql_insert)
                conn.commit()
                print('data is updated')
                print('******************************************')




            elif choice == 12 :
                y = 0
                print('******************************************')
                a = input('Enter your product name: \n')
                t = 'select*from stock where Name=("{}")'.format(a)
                c.execute(t)
                v=c.fetchall()
                for i in v:
                    print(v)
                    y +=1
                if y == 0:
                    print("Not Found")
                print('******************************************')

                


            elif choice == 13:
                print('******************************************')
                engine = pyttsx3.init()
                engine.say("Thank you for using programme , Programme Terminated")
                engine.runAndWait()
                print('******************************************')
                break


        else:
            print('wrong password, try again ')
            engine = pyttsx3.init()
            engine.say("wrong password, try again")
            engine.runAndWait()
            break


    
        


if choice==2:
    exit()



