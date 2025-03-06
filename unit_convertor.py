import streamlit as st
import base64

# Dictionary storing classmates and your thoughts about them
classmate_thoughts = {

            #hareem
    "hareem": "You’ve got beauty, brains, and a master’s degree in 'How to Get People to Do Your Work'—all without lifting a finger! 😏 If management was an Olympic sport, you’d have more gold medals than Usain Bolt. 🏅 Teachers adore you so much, we’re pretty sure they’d adopt you if they could. 😂 Wherever you go, whatever you do, one thing is guaranteed—there will be a reel! 🎥✨ Your Punjabi accent adds extra spice to everything you say 🌶️, and let’s not forget your obsession with that big-nose emoji—maybe 🤥 it’s your spirit animal? 🤭 But beneath all that mastermind-level manipulation, you have a soft spot for your endless army of nieces and nephews who drive you crazy but also own your heart.  A true mix of beauty, brains, and ‘bhanjay-bhanjiyan’ chaos! 🤣🔥",

    #hamna 

    "hamna":"You are so breathtakingly beautiful that even Instagram filters feel unemployed around you. 🤩✨ Your eyes could probably hypnotize people into doing your assignments, and that smile? It’s a weapon of mass destruction—melting hearts and dodging trouble since day one. 💖 But let’s be honest, if beauty was a subject, you’d ace it, but physics? That’s your villain origin story. 📚😭Your aesthetic sense is so strong that even your water bottle probably matches your outfit. 💦😂 Speaking of water, you drink so much of it that even the ocean feels under-hydrated. 🌊 But hey, at least your skin stays flawless while the rest of us survive on caffeine and regret.You admire everyone’s work like an angel 😇, but when it comes to ‘tabsora’ (explanations), your brain just files for bankruptcy. 😵‍💫 And the best part? You have the rare talent of telling teachers they’re bad at teaching—with a smile so sweet that they actually thank you for it. 😆👏 A true legend in the art of roasting with politeness! 🔥😂",

              #umme habiba


    "umme habiba":"You are so brilliant in studies that even Google might ask you for answers someday. 📚🤯 While the whole class is busy joking and causing chaos, you sit there with laser-sharp focus like a monk on a mission. 🧘‍♀️📖 Seriously, if concentration had a face, it would be yours—unbothered, undistracted, and unstoppable.But don’t be fooled by your studious vibe! You have a roast game so strong that even the best comedians would take notes. 🎤🔥 The best part? You never even think bad about anyone—you serve respectful insults with so much class that people actually enjoy getting roasted by you. 😂👏And when you’re not busy being a genius or roasting souls, you’re lost in novels and poetry, living in a world where reality stands no chance. 📖✨ Your humor is so top-tier that even life’s worst moments become memes in your mind. Honestly, if intelligence, wit, and sarcasm had a fan club, you’d be the president. 🤓😂",

        #Rubab

    "rubab":"You have an unstoppable talent—turning the most normal sentence into a full-blown comedy show without even trying. 😂🎤 Seriously, if accidental jokes were a career, you’d be a billionaire by now! You talk sooooo much that even a podcast would beg for a break. 🎙️🫠 But the funny part? You don’t even realize half the things you say are hilarious!Despite being a non-stop chatterbox, you’re also the shyest person ever. Like, how does that even work? 🤔 One second, you’re talking for hours, and the next, you’re blushing like someone just exposed your search history. And let’s not ignore your legendary Snapchat filter addiction—girl, you don’t just use filters on yourself, you even put them on pakoras! 🤳😂 Like, why does a snack need a beauty mode? Is the pakora going to a wedding? 🤔💅✨ Even your chai has probably had a virtual glow-up at this point. ☕😂",
        

        #zainab

"zainab":"You are basically a walking, talking WWE match—if there’s no argument in a day, it’s like your system crashes. 💥😂 Jhagralu? More like Jhagra Queen! 👑 If there was a degree in 'Fasaad Machana,' you'd have a PhD by now. You don’t just pull people’s legs—you drag them into a full-blown wrestling ring! 😂🎤.But let’s be fair, your cooking skills are top-notch. 🍲🔥 You can whip up a delicious meal right after roasting someone in an argument—talk about balance! And when it comes to gossip, you don’t just spill the tea, you pour the entire kettle. ☕😆Oh, and your Islamic side—let’s just say, you follow only the parts that suit you. The rest? Jee, wo maaf hain! 🤲😂 And college? You hate it so much that if Behbud College had a “Biggest Hater” award, you’d win every year. 🎖️Also, why are you always in a battle with your own fingers and foot? 😭 Like, what have they done to you? Leave them alone! 😂 But despite all this drama, life would be sooo boring without your daily jhagras and expert-level gossip. Keep being the spicy, savage, and slightly halal troublemaker that you are!",


 # Alisha


"alisha":"You are basically the CEO of management—whether it’s handling tasks, people, or showing off mid-conversation, you do it all with perfect precision! 😎✨ No matter what we’re talking about, you’ll somehow slip in a flex so smoothly that we almost don’t notice… almost. 😂Born to be a front-bencher, you sit there like a dedicated teacher’s chamcha, nodding along to every word as if it’s the most groundbreaking knowledge ever shared. 🤓📚 While others secretly nap or doodle, you stare directly at the teacher, absorbing every second of the lecture without a blink. How do you not get bored?! 😭And let’s not forget, you’re a total mummy-daddy type—rules? ✅ Respect? ✅ Proper behavior? ✅But jokes aside, your politeness, discipline, and way of handling situations gracefully make you truly stand out. 🌟 You know how to talk to everyone with kindness, and even if there’s a little show-off mode activated, we all know it’s just part of your charm. Keep ruling the front row and managing life like a pro! 👏😂",


# hafsa zulfiqar


"hafsa zulfiqar":"You are the undercover study machine—secretly focused on books while being the ultimate ratta master! 📚 Your answers are so long that even the paper gets tired, but concepts? Let’s not go there. 😂Your desi fashion sense is unmatched—whether it's a wedding or a random college day, you show up like a walking jewelry shop with layers of makeup and an outfit brighter than the sun. ☀️💃Shy to the core, never seen in extracurriculars, yet somehow the math teacher’s favorite! Maybe it’s your endless answer sheets or just pure luck. Either way, you're a silent warrior—focused, fashionable, and the queen of 'one more point left' in exams! 😂🔥",


# jaweria arif

"jaweria arif":"You are the perfect combination of beauty and chaos! 😆 With your long, flowing hair, you could be in a shampoo commercial—until you scream. That’s when the world regrets having ears. 😂You hate studying, yet your grades mysteriously stay up—maybe it's talent, maybe it's luck, or maybe the teachers just gave up trying to understand how. 🤷‍♀️As the ultimate backbencher, you’re more famous than the toppers—just not for the right reasons. Every teacher knows you, but not as their 'star student'… more like the 'why is she always in trouble?' student. And of course, your clothes? Never complete without a fresh splash of neel—it's your unintentional signature style! 💙😂",

#hafsa

"hafsa naseer":"You are a pure soul with a heart full of love for your mom and family—but let’s be honest, your love for trouble is just as strong. 😂 No matter how hard you try, you always end up with a bruise or two—like life itself is playing ‘tag’ with you.Confident in your looks? Absolutely! But if height could be ordered online, you’d be the first to check out. 😆 You hate studying, but the real challenge? Holding in your laughter when the teacher is yelling—it’s like your brain hears ‘serious moment’ and responds with ‘let’s giggle.’ 🤭You love exercise—in theory. Execution? Eh, maybe next week. And when it comes to chatting, the moment you see a long text, it’s an instant 'I'll reply later' situation. 😅 But when it’s time to speak your mind, you have no filter—you’ll say anything to anyone, and somehow, still survive. 💀😂",

#shabana

"shabana":"You and math have the worst love story—no matter how hard you try, it just refuses to love you back. 😂 But one thing you never fail at? Guarding your seat like a treasure chest! No one dares to take it unless they have a death wish. 😆Jokes? Yeah… let’s not go there. While everyone is laughing, you’re already planning a revenge speech. 🤡 But at least you’re real—no fake smiles, no double standards, just pure simplicity. ✨ And let’s not forget the most important part—Friday snack duty! 🍟🍫 No one knows how or why, but you always show up with treats for everyone, securing your VIP status in the group. 😎🔥",


#Musfira

"musfira":"Once you say something, it's final—even if the whole world proves you wrong, you're standing your ground like a true warrior. 😂 You come to school so rarely that it feels like you're just visiting your grandma’s house once a week for fun. 🎒🏡But when it comes to math, you’re an absolute genius! 🧠✏️ Numbers fear you, but your weight scale doesn’t—because, well… where are you even hiding all that brain power in such a thin frame? 🤷‍♀️😆.And let’s not even talk about your unstoppable speech mode—once you start, even the teacher gives up. 🎤😂 Also, your show-off skills? Elite! 😎 And don’t even think about sitting at her computer in the lab—unless you want to get disowned as a friend. 💻🚫",

# sumaiya

"sumaiya":"She is the definition of grace with guts! 💪✨ Firm in her Islamic values 🕌, a proud supporter of Jamaat-e-Islami 🟢, and absolutely fearless when it comes to defending what she believes in—say anything against them, and congratulations, you just signed up for a never-ending debate 🎤🔥. But despite her strong opinions, she is beautiful inside and out 😍, always friendly and kind to everyone. However, don’t mistake her kindness for silence—if she sees something wrong, she will call it out on the spot ⚖️, no hesitation, no sugarcoating. And when she somehow ends up in trouble with teachers (which, let’s be honest, happens 🤭), her perfect tone and innocent smile 😇✨ work like magic—suddenly, she’s not the guilty one, but the misunderstood one 🤷‍♀️😂. A true mix of conviction, charm, and cleverness! 💫",

#nadra

"nadra":"She’s the queen of comfort over fashion 👕👖—if it’s not cozy, she’s not wearing it! With her small eyes 👀 and a naturally shy personality, she might seem quiet at first, but oh boy, when she talks, she drops random facts like she has a PhD in everything 🎓—even if she just learned about it five seconds ago. 🤣 The way she sits on the desk, folding herself into a human pretzel 🌀, makes you wonder if she’s attending class or preparing for a yoga competition. Academics? Not her strongest area 📚❌, but confidence? Unlimited! And of course, how can we forget her most iconic dialogue—“Me apne aap se bezar hun” 😩, making everyone wonder if she’s serious or just being dramatic. 🤭😂",


#Laiqa
"laiqa":"Her English is a crime scene—grammar murdered, spelling missing, and tenses all fighting for their lives! 😂📖 But give her credit, she never gives up—still out here battling the Oxford Dictionary like a warrior. 💪😂 And her fashion sense? Oh, she’s living in 2025 but accessorizing like it’s her chachi’s era—that nose ring and aunty-style ear tops are her signature look! 💍👂 If “shaadi season” had a brand ambassador, it would be her. 🤣.But wait, her real hidden talent? Listening. 👂✨ While the rest of us are just waiting for our turn to talk, she actually lets people finish their sentences without jumping in—like, what kind of sorcery is that?! 😳😂 She may be bad at English, but she’s got patience, style (questionable), and determination—and honestly, that’s a power combo! 🚀👏"





}

# Function to set background image with blur effect
def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    encoded_image = base64.b64encode(img_data).decode()

    st.markdown(
        f"""
        <style>
         @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');
        .stApp {{
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.9)), 
                        url("data:image/png;base64,{encoded_image}") no-repeat center center fixed;
            background-size: cover;
        }}

        /* Blur effect */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: inherit;
            filter: blur(10px);  /* Adjust blur intensity */
            z-index: -1;
        }}

        /* Make title and input label white */
        h1, label,.warning {{
            color: white !important;
            text-align: center;
        }}
        .custom {{
        font-family: cursive;}}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image (Replace with your actual image file)
set_background("background.jpg")

# Streamlit UI
st.markdown("<h1 class='custom'>The Roast Machine</h1>", unsafe_allow_html=True)

# Input field for name
name = st.text_input("Enter your name (in lower case):")

# Show paragraph if name exists
if name:
    if name in classmate_thoughts:
        st.markdown(f"<p style='color: white; font-size: 18px; text-align: center;'><b>☕ Spilling the Tea on You</b><br>{classmate_thoughts[name]}</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<p class='warning'> Sorry, I haven't written anything about you yet! 😅</p>",unsafe_allow_html=True)
