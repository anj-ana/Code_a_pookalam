c = circle(r=150,fill="#541e07",stroke="none")+circle(r=130,fill="#690b07",stroke="none")+circle(r=110,fill="#962109",stroke="none")+circle(r=52,fill="#520439",stroke="#260002",stroke_width=2)
r1=rectangle(w=100,h=25,x2=15,y2=0,fill="#e01d65",stroke="#fffafa",stroke_width=3) | repeat(4,rotate(60))
e1=ellipse(w=80,h=15,x2=15,y2=0,fill="#d6cf09",stroke="none") | repeat(4,rotate(60))
r2=rectangle(w=37,h=15,x=70,y=0,fill="#8e2999",stroke="#203016",stroke_width=2) | repeat(36,rotate(10))
l1=line(x1=106,y1=0,x2=150,y2=0,stroke="#b58800",stroke_width=3.5) | repeat(12,rotate(30))
c1=circle(r=5,x=100,y=0,fill="#0aecf0")| repeat(12,rotate(30))
show(c,r1,e1,r2,l1,c1)
