
def motivation():
    """Get inspiring quotes to fuel up the user and to motivate him/her in there financial pursuit"""

    import random
    quote_1 = """Time is more valuable than money. You can get more money, but you cannot get more time.~Jim Rohn """
    quote_2 = """“The person who doesn't know where his next dollar is coming from usually doesn't know where his last 
    dollar went.” """
    quote_3 = """“It doesn’t matter about money; having it, not having it. Or having clothes, or not having them. You’re 
    still left alone with yourself in the end.” Billy Idol """

    quote_4 = """ “Money does not buy you happiness, but lack of money certainly buys you misery.”
    Daniel Kahneman"""

    quote_5 = """ “Expect the best. Prepare for the worst. Capitalize on what comes.”
    Zig Ziglar"""

    quote_6 = """“It’s good to have money and the things that money can buy, but it’s good, too, to check up once in a 
    while and make sure that you haven’t lost the things that money can’t buy.” George Lorimer """

    quote_7 = """“Making money is a common sense. It’s not rocket science. But unfortunately, when it comes to money, 
    common sense is uncommon.” Robert Kiyosaki """

    quote_8 = """ “That man is richest whose pleasures are cheapest.”
    Henry David Thoreau"""

    quote_9 = """“The money you have gives you freedom; the money you pursue enslaves you.”
    Jean-Jacques Rousseau"""

    quote_10 = """“Money is multiplied in practical value depending on the number of W’s you control in your life: what 
    you do, when you do it, where you do it, and with whom you do it.” Tim Ferriss """

    quote_11 = """“I will tell you the secret to getting rich on Wall Street. You try to be greedy when others are 
    fearful. And you try to be fearful when others are greedy.” Warren Buffett """

    quote_12 = """“They deem me mad because I will not sell my days for gold; and I deem them mad because they think my 
    days have a price.” Kahlil Gibran """

    quote_13 = """ “The real measure of your wealth is how much you’d be worth if you lost all your money.”
    Unknown"""

    quote_14 = """“He who loses money, loses much; He who loses a friend, loses much more; He who loses faith, loses all.”
    Eleanor Roosevelt """

    quote_15 = """“Happiness is not in the mere possession of money; it lies in the joy of achievement, in the thrill of 
    creative effort.” Franklin D. Roosevelt """

    quote_16 = """ “To acquire money requires valor, to keep money requires prudence, and to spend money well is an art.”
    Berthold Auerbach"""

    quote_list = [quote_1, quote_2, quote_3, quote_4, quote_5, quote_6, quote_7, quote_8, quote_8, quote_9, quote_10,
                  quote_11, quote_12, quote_13, quote_14, quote_15, quote_16]

    quote_computer_choice = random.choice(quote_list)

    return quote_computer_choice

