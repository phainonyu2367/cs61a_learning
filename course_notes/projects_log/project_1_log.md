project_1_hog 复盘记录
## 应该学会/记住什么东西？
1. 模块化/函数化开发
	在python中函数传参和定义十分容易，多多使用函数来闭包功能能够使过程更加清晰，更于简捷易懂。
2. 养成日志或者记录的习惯
	当工程规模逐渐扩大的时候，我们很容易忘记函数的功能，输入和输出，所以我们需要一个log来记录。区别于docstring，docstring是解释函数运行的基本逻辑，以便于以后的维护，log应当描述的是整个文件的基本运行流程。这个习惯一定要养成，因为这对以后的开发有着很大的帮助。
3. 纯函数程序
	```
	def announce_lead_changes(last_leader=None):

    """Return a commentary function that announces lead changes.

  

    >>> f0 = announce_lead_changes()

    >>> f1 = f0(5, 0)

    Player 0 takes the lead by 5

    >>> f2 = f1(5, 12)

    Player 1 takes the lead by 7

    >>> f3 = f2(8, 12)

    >>> f4 = f3(8, 13)

    >>> f5 = f4(15, 13)

    Player 0 takes the lead by 2

    """

    def say(score0, score1):

        if score0 > score1:

            leader = 0

        elif score1 > score0:

            leader = 1

        else:

            leader = None

        if leader != None and leader != last_leader:

            print('Player', leader, 'takes the lead by', abs(score0 - score1))

        return announce_lead_changes(leader)

    return say
	```
	以这个函数为例，我们可以初见函数式编程的特点并引入函数状态机的概念。简单的理解，这里的函数状态机相当于用函数自身迭代来传递信息并更新状态。像上面这个函数，它就相当于每次结算（print完）之后就会返回一个新的状态（不同配置的高阶函数（工厂）），这样下一个函数状态就会包含先前的状态并输出新的结果。
>那这种写法在哪里用到呢？

>[!info]
>|场景|解释|为什么不用变量|
|---|---|---|
|**要保存状态但不能用全局变量**|CS61A/Hog commentary|避免污染命名空间|
|**想要不可变状态（pure FP）**|时间线式状态链|更安全，不会被意外修改|
|**想组合多个行为**|combine_commentaries|函数之间的组合更简单|
|**写解释器、模拟器、状态机**|parser/tokenizer|状态天然沿着调用传递|
