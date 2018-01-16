# ChatBot

## Documentation

ChatterBot是一个Python库，可以轻松生成对用户输入的自动响应。 ChatterBot使用一系列机器学习算法来产生不同类型的响应。 这使开发人员可以轻松创建聊天机器人并自动与用户进行对话。 有关ChatterBot背后的思想和概念的更多细节，请参阅[流程图](http://chatterbot.readthedocs.io/en/stable/#process-flow-diagram)。

示例：

```
user: Good morning! How are you doing?
bot:  I am doing very well, thank you for asking.
user: You're welcome.
bot:  Do you like hats?
```

## 语言独立

ChatterBot的独立于语言的设计使其能够训练成对任何语言都适用。 此外，ChatterBot的机器学习特性允许代理实例在与人类和其他信息数据源进行交互时提高自己对响应的准确性。

## ChatterBot是如何工作的

ChatterBot是一个Python库，用于创建可以参与对话的软件。   

一个未经训练的ChatterBot[实例](一个未经训练的ChatterBot实例开始时不知道如何沟通。 每次用户输入一个语句时，库都会保存它们输入的文本以及语句响应的文本。 随着ChatterBot收到更多的输入，它可以回复的响应数量和每个响应相对于输入语句的准确度都会增加。)开始时不知道如何沟通。 每次用户输入一个[语句](http://chatterbot.readthedocs.io/en/stable/glossary.html#term-statement)时，库都会保存它们输入的文本以及语句响应的文本。 随着ChatterBot收到更多的输入，它可以回复的响应数量和每个响应相对于输入语句的准确度都会增加。

程序通过搜索匹配输入的最接近匹配的已知语句来选择最接近的匹配响应，然后从响应中选择一个返回。

## 流程图

## 快速开始

### 创建一个新聊天机器人

```
from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
```

### 训练

创建一个新的ChatterBot实例后，就可以训练机器人。 训练是一个很好的方法，以确保机器人开始了解具体的反应的知识。 当前的训练方法采用代表对话的语句列表。 其他说明可以在[训练](http://chatterbot.readthedocs.io/en/stable/training.html#set-trainer)文档中找到。

*训练不要求但是推荐*

```
from chatterbot.trainers import ListTrainer

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
```

### 获得响应

```
response = chatbot.get_response("Good morning!")
print(response)
```

## ChatterBot教程

本教程将指导您使用ChatterBot创建简单的命令行聊天机器人。

### 获得帮助

如果您在本教程中遇到问题，可以在[Gitter](https://gitter.im/chatter_bot/Lobby)上发布消息与其他可能帮助的ChatterBot用户聊天。

### 创建你第一个机器人

`from chatterbot import ChatBot`
`bot = ChatBot('Norman')`

这行代码创建了一个名为Norman的新的聊天机器人。 在我们第一次运行我们的程序之前，我们会指定更多的参数。

### 设置存储适配器（storage adapter）

ChatterBot带有内置的适配器类，允许它连接到不同类型的数据库。 在本教程中，我们将使用允许聊天机器人连接到SQL数据库的`SQLStorageAdapter`。 默认情况下，这个适配器将创建一个SQLite数据库。

数据库参数用于指定聊天机器人将使用的数据库的路径。 对于这个例子，我们将调用数据库database.sqlite3。 如果该文件不存在，该文件将被自动创建。

```
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database='./database.sqlite3'
)
```

*SQLStorageAdapter是ChatterBot的默认适配器。 如果您不在构造函数中指定适配器，则将自动使用SQLStorageAdapter适配器。*

### 输入和输出适配器

接下来，我们将添加参数来指定输入和输出终端适配器。 输入终端适配器只是从终端读取用户的输入。 输出终端适配器打印聊天机器人的响应。

```
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./database.sqlite3'
)
```

### 指定逻辑适配器

*logic_adapters*参数是一个逻辑适配器列表。 在ChatterBot中，逻辑适配器是一个接受输入语句并返回该语句的响应的类。

您可以选择使用尽可能多的逻辑适配器。 在这个例子中，我们将使用两个逻辑适配器。 TimeLogicAdapter返回输入语句要求的当前时间。 MathematicalEvaluation适配器解决了使用基本操作的数学问题。

```
bot = ChatBot(
    'Norman',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database='./database.sqlite3'
)
```

### 从你的机器人获得响应

接下来，您将需要创建一个while循环让您的聊天机器人运行。当特定的异常被触发时，通过跳出循环，当用户进入ctrl + c时，我们可以退出循环并停止程序。

```
while True:
    try:
     bot_input = bot.get_response(None)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
```

### 训练你的聊天机器人

你的聊天机器人Norman将学习与你交谈时的沟通。 你可以通过训练他现有的对话示例来加速这个过程。

```
bot.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])
```

您可以多次运行训练过程，以强化对特定输入语句的首选回答。 您还可以在许多不同的示例对话框上运行train命令，以增加聊天机器人可以响应的输入的广度。

------

## 示例

### 简单示例

```
# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    trainer='chatterbot.trainers.ListTrainer'
)

chatbot.train([
    "Hi, can I help you?",
    "Sure, I'd like to book a flight to Iceland.",
    "Your flight has been booked."
])

# Get a response to the input text 'How are you?'
response = chatbot.get_response('I would like to book a flight.')

print(response)
```

### 终端示例

这个示例程序演示了如何创建一个简单的终端客户端，使您能够通过在终端中键入来与您的聊天机器人通信。

```
# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
        "chatterbot.logic.BestMatch"
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="../database.db"
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
```

### 使用MongoDB

在您可以使用ChatterBot的MongoDB内置适配器。但是之前，您需要[安装MongoDB](https://docs.mongodb.com/manual/installation/)。 在执行你的程序之前，确保MongoDB正在你的环境中运行。 要告诉ChatterBot使用这个适配器，你将需要设置storage_adapter参数。