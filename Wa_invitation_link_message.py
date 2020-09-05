print("script by ShoeraRei");
wa_link = "https://wa.me/";
number_phone = int(input ("enter phone number without \"+\" :"));
message = input("your message :");
join = wa_link+str(number_phone)+"?text="+message.replace(" ","%20");

print("copy this limk \n"+join);