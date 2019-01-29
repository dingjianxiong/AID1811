class Dog:
    def eat(self,food):
        print(self.color,"的",self.kinds,"小狗正在吃：",food)
        self.last_food=food#让每次吃食物的狗记住吃的是什么
    def food_info(self):
        print(self.color,"的",self.kinds,"小狗上次吃的是：",self.last_food)

dog1=Dog()#创建一个示例
dog1.color='白色'#为dog1对象添加color属性，绑定”白色“
dog1.kinds='京巴'#添加”kind属性
dog1.eat("骨头")

dog2=Dog()
dog2.color="灰色"
dog2.kinds="哈士奇"
dog2.eat("狗粮")

# print(dog1.color,"的",dog1.kinds)

dog1.food_info()#显示dog1上次吃的什么
dog2.food_info()