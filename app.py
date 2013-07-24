#~*~ coding: utf-8 ~*~
from random import choice
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'bon jour. <a href="{}">a joke.</a>'.format(url_for('jokes'))


@app.route('/jokes')
def jokes():
    """all stolen: http://www.quora.com/Humor/What-is-the-geekiest-joke"""

    joke_list = [
        "Yo momma's so mean, she has no standard deviation.",
        "Heisenberg gets pulled over by the police. The cop asks, 'Do you know how fast you were going?' Heisenberg responds, 'No, but I know exactly where I am!'",
        "Girlfriend: Honey, I cant open this jar / Geek Boyfriend: Try reinstalling java",
        "Yo mamma is so old Debian has marked her a stable release",
        "Q: Why do programmers always mix up Halloween and Christmas? / A: Because Oct 31 == Dec 25!",
        "'Knock, knock.' / Who’s there?' / very long pause... / 'Java.'",
        "Q: 'Whats the object-oriented way to become wealthy?' / A: Inheritance",
        "'Lets talk about potassium' / 'K.'",
        "I'd tell you a UDP joke but you might not get it.",
        "If you're not part of the solution, you're part of the precipitate.",
        "Assume we have 1000 apples, or let's take a round figure, 1024 apples.",
        "Q: What do you get when you cross a mosquito with a rock climber? / A: Nothing. You can't cross a vector and a scalar.",
        "Why does python live on land? / Because it is above C level..",
        "Never trust an atom.  They make up everything.",
        "He said I was just average. How mean.",
        "Three perfect logicians walk into a bar. The bartender asks 'Do all of you want a beer?' The first logician says 'I don't know'. The second logician says 'I don't know'. The third logician says 'Yes!'",
        "Q: Why don't humanities majors want to work with UNIX? / A: Because they don't want to be eunuchs.",
        "Q: What is non-orientable and lives in the ocean? / A: Möbius Dick",
        "Q: What's purple and commutes? / A: An Abelian grape",
        "As a child, I was obsessed with the difference between sine and cosine. As I got older, I realized it was just a phase.",
        "What's an anagram of Banach-Tarski? Banach-Tarski Banach-Tarski.",
        "Q: How many designers does it take to screw in a light bulb? / A: Does it have to be a light bulb?",
        "Did you hear about the restaurant NASA is starting at the Moon? Great food, but no atmosphere.",
        "Some people say the glass is half full. / Some people say the glass is half empty. / Engineers say the glass is twice as big as necessary.",
        "Two chemists walk in to a chemistry bar. The first one said 'I'll take some H2O, please' and the second said 'I'll take some H20 too, please.' Second one died.",
        "I used to be an astronomer but I got stuck on the day shift.",
        "A room temperature super conductor walks into the bar. The bartender says 'We don't serve room temperature super conductors here.' The room temperature super conductor leaves without putting up any resistance.",
        "Schroedinger's Cat walks into a bar...and doesn't.",
        "A neutrino walks into a bar. The bartender says 'We don't serve neutrinos in this bar.' The neutrino says 'Hey, I was just passing through.",
        "Some Helium gas drifts into the bar. 'The bartender says we don't serve Helium.' The Helium doesn't react.",
        "Let epsilon be an integer.",
        "The bartender says \"We don't serve Tachyons here\". A Tachyon walks into a bar.",
        "Bartender: 'Get out! We don't serve beer to faster than light subatomic particles !!' / A neutrino enters the bar.",
        "Wanted Schrödinger's cat. Dead xor Alive.",
        "A programmer's wife asks him to go to the store and pick up a stick of butter, and while he's there, pick up eggs. / He never returned.",
        "The box said ‘Requires Windows Vista or better’. So I installed LINUX.",
        "If at first you don’t succeed; call it version 1.0.",
        "Why did the chicken cross the Möbius strip? To get to the same side.",
        "An SQL query walks into a bar and sees two tables. She walks up to them and says, 'mind if I join you?'.",
        "An SEO expert walks into a bar, bars, beer garden, hangout, lounge, night club, mini bar, bar stool, tavern, pub, beer, wine, whiskey...",
        "A neutron walked into a bar and asked, 'How much for a drink?' The bartender replied, 'For you, no charge.'",
        "There are two types of people in this world.  Those who like closure, and",
    ]
    return '<a href="{}"><< back home</a><br/>{}'.format(
        url_for("home"), choice(joke_list))


@app.route('/secret-page')
def cant_find_this():
    return "obscurity is not security"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
