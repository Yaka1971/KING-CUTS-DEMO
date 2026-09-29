from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "images")
AUDIO_DIR = os.path.join(BASE_DIR, "AUDIO")

PAGE = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KING'S CUTS | Barbershop</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&display=swap');
:root{--black:#050505;--gold:#d8a53c;--gold-light:#ffd777;--white:#f7f7f7}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#050505;color:#f7f7f7;font-family:Arial,sans-serif;overflow-x:hidden}a{text-decoration:none;color:inherit}
header{position:fixed;top:0;left:0;width:100%;height:82px;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:0 5%;background:rgba(4,4,4,.93);border-bottom:1px solid rgba(216,165,60,.35);backdrop-filter:blur(15px)}
.logo{display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:190px;line-height:1}
.logo-crown{color:var(--gold-light);font-size:25px;line-height:.7;margin-bottom:5px;text-shadow:0 0 12px rgba(216,165,60,.25)}
.logo-main{font-family:"Cinzel",Georgia,serif;font-size:22px;font-weight:700;letter-spacing:.4px;color:var(--gold-light);white-space:nowrap}
.logo-main span{color:var(--gold-light)}
.logo-sub{display:flex;align-items:center;gap:8px;color:var(--gold-light);font-family:"Cinzel",Georgia,serif;font-size:7px;font-weight:600;letter-spacing:5px;margin-top:6px}
.logo-sub:before,.logo-sub:after{content:"";display:block;width:22px;height:1px;background:var(--gold)}
nav{display:flex;gap:27px}nav a{font-size:11px;font-weight:700;letter-spacing:1px}.sound-button{border:1px solid var(--gold);background:#000;color:var(--gold-light);padding:11px 16px;border-radius:50px;font-size:10px;font-weight:800;cursor:pointer}.sound-button.active{background:var(--gold);color:#000}
.hero{min-height:700px;padding:0;display:block;position:relative;background:#050505;overflow:hidden}
.hero-copy{position:absolute;z-index:5;left:6%;top:50%;transform:translateY(-50%);max-width:600px;padding:32px;background:linear-gradient(90deg,rgba(0,0,0,.88),rgba(0,0,0,.45),transparent);text-shadow:0 3px 20px #000}
.eyebrow{color:var(--gold-light);font-size:11px;font-weight:700;letter-spacing:5px;margin-bottom:18px}
.hero h1{margin:0;font-size:clamp(68px,7vw,116px);line-height:.88;text-transform:uppercase}
.hero h1 .gold{display:block;color:var(--gold-light);text-shadow:0 0 25px rgba(216,165,60,.23)}
.hero-description{margin-top:27px;max-width:550px;color:#e1e1e1;line-height:1.7;font-size:15px}
.hero-buttons{margin-top:31px;display:flex;gap:14px;flex-wrap:wrap}
.btn{display:inline-flex;padding:16px 23px;border:1px solid var(--gold);font-size:11px;font-weight:800}
.btn-gold{background:var(--gold);color:#000}.btn-dark{background:#090909}
.hero-visual{width:100%;height:700px;position:relative;overflow:hidden}
.hero-visual img{width:100%;height:100%;object-fit:cover;display:block}
.hero-visual:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.72) 0%,rgba(0,0,0,.30) 42%,rgba(0,0,0,.05) 72%,rgba(0,0,0,.18) 100%)}
.hero-stamp{position:absolute;z-index:4;right:4%;bottom:35px;background:rgba(0,0,0,.78);border-left:3px solid var(--gold);padding:17px 20px}
.hero-stamp strong{display:block;color:var(--gold-light)}
.cuts-section{position:relative;min-height:650px;overflow:hidden;background:radial-gradient(circle at 50% 45%,rgba(216,165,60,.08),transparent 35%),#050505;border-top:1px solid rgba(216,165,60,.5);border-bottom:1px solid rgba(216,165,60,.5);padding:115px 4% 70px}
.cuts-header{position:absolute;z-index:50;top:38px;left:0;width:100%;text-align:center}
.cuts-header small{color:var(--gold);font-size:10px;font-weight:800;letter-spacing:5px}
.cuts-header h2{margin:6px 0 0;font-size:54px}
.cut-stage{position:relative;width:100%;height:470px;overflow:hidden}
.cut-slide{position:absolute;top:50%;width:min(27vw,390px);aspect-ratio:1/1;opacity:0;transform:translateY(-50%) scale(.97);transition:opacity 1.55s ease,transform 1.55s ease;pointer-events:none;border:1px solid rgba(216,165,60,.4);box-shadow:0 18px 55px rgba(0,0,0,.7);background:#080808;display:block}
.cut-slide img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.cut-slide:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 60%,rgba(0,0,0,.15));pointer-events:none}
.cut-information,.cut-number,.cut-name,.cut-description{display:none}
.gold-flash{position:absolute;z-index:45;inset:0;pointer-events:none;opacity:0;background:linear-gradient(115deg,transparent 20%,rgba(255,211,113,.08) 38%,rgba(255,211,113,.72) 49%,rgba(255,255,255,.75) 50%,rgba(255,211,113,.25) 53%,transparent 70%);transform:translateX(-100%)}.gold-flash.flash{animation:flashSweep .75s ease}@keyframes flashSweep{0%{opacity:0;transform:translateX(-100%)}30%{opacity:.65}100%{opacity:0;transform:translateX(100%)}}
.services{padding:85px 6%;background:#090909}.section-title{text-align:center;margin-bottom:50px}.section-title small{color:var(--gold);letter-spacing:5px;font-size:10px}.section-title h2{font-size:48px;margin:8px 0}.service-grid{display:grid;grid-template-columns:repeat(6,1fr);border-top:1px solid #59451e;border-bottom:1px solid #59451e}.service{padding:35px 20px;text-align:center;border-right:1px solid #3b301b}.service-icon{font-size:31px}.service h3{font-size:13px}.service p{color:#999;font-size:11px}
.mission{display:grid;grid-template-columns:1fr 1fr;min-height:520px}.mission-image{min-height:520px;background:url("/images/kc_shop.png") center/cover no-repeat}.mission-copy{padding:80px 8%;display:flex;flex-direction:column;justify-content:center}.mission-copy small{color:var(--gold);letter-spacing:5px}.mission-copy h2{font-size:60px;line-height:.95;margin:10px 0}.mission-copy h2 span{color:var(--gold-light)}.mission-copy p{color:#bbb;line-height:1.8}
.quote{padding:100px 7%;text-align:center;background:linear-gradient(135deg,#050505,#17120a,#050505)}.quote h2{font-size:clamp(35px,5vw,65px)}.quote h2 span{color:var(--gold-light)}

.booking{padding:95px 6%;background:radial-gradient(circle at 50% 0%,rgba(216,165,60,.10),transparent 38%),#080808;border-top:1px solid rgba(216,165,60,.35)}
.booking-wrap{max-width:1050px;margin:0 auto}
.booking-heading{text-align:center;margin-bottom:45px}
.booking-heading small{color:var(--gold);font-size:10px;font-weight:800;letter-spacing:5px}
.booking-heading h2{font-family:"Cinzel",Georgia,serif;font-size:clamp(42px,5vw,68px);margin:9px 0 12px;color:#fff}
.booking-heading h2 span{color:var(--gold-light)}
.booking-heading p{max-width:650px;margin:0 auto;color:#aaa;line-height:1.7}
.booking-form{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;padding:35px;border:1px solid rgba(216,165,60,.38);background:rgba(3,3,3,.88);box-shadow:0 20px 70px rgba(0,0,0,.45)}
.form-group{display:flex;flex-direction:column;gap:8px}
.form-group.full{grid-column:1/-1}
.form-group label{color:var(--gold-light);font-size:9px;font-weight:800;letter-spacing:2px}
.form-group input,.form-group select,.form-group textarea{width:100%;border:1px solid #3b301b;background:#0c0c0c;color:#f7f7f7;padding:15px 14px;font:inherit;outline:none;transition:border-color .2s ease,box-shadow .2s ease}
.form-group input:focus,.form-group select:focus,.form-group textarea:focus{border-color:var(--gold);box-shadow:0 0 0 2px rgba(216,165,60,.10)}
.form-group textarea{min-height:115px;resize:vertical}
.booking-submit{grid-column:1/-1;border:1px solid var(--gold);background:var(--gold);color:#050505;padding:17px 24px;font-weight:900;letter-spacing:1px;cursor:pointer}
.booking-submit:hover{background:var(--gold-light)}
.booking-success{display:none;grid-column:1/-1;text-align:center;padding:25px;border:1px solid rgba(216,165,60,.5);background:rgba(216,165,60,.08)}
.booking-success strong{display:block;color:var(--gold-light);font-family:"Cinzel",Georgia,serif;font-size:22px;margin-bottom:8px}
.booking-success span{color:#bbb;font-size:13px}

footer{padding:45px 6%;display:flex;justify-content:space-between;gap:25px;background:#030303;border-top:1px solid #493719;color:#777;font-size:10px}.footer-brand{display:flex;flex-direction:column;align-items:center;justify-content:center;min-width:190px;line-height:1}
.footer-brand .logo-crown{color:var(--gold-light);font-size:25px;line-height:.7;margin-bottom:5px;text-shadow:0 0 12px rgba(216,165,60,.25)}
.footer-brand .logo-main{font-family:"Cinzel",Georgia,serif;font-size:22px;font-weight:700;letter-spacing:.4px;color:var(--gold-light);white-space:nowrap}
.footer-brand .logo-sub{display:flex;align-items:center;gap:8px;color:var(--gold-light);font-family:"Cinzel",Georgia,serif;font-size:7px;font-weight:600;letter-spacing:5px;margin-top:6px}
.footer-brand .logo-sub:before,.footer-brand .logo-sub:after{content:"";display:block;width:22px;height:1px;background:var(--gold)}
@media(max-width:1000px){nav{display:none}.hero{grid-template-columns:1fr}.service-grid{grid-template-columns:repeat(3,1fr)}.mission{grid-template-columns:1fr}}
@media(max-width:650px){
header{height:70px;padding:0 18px}
.sound-button{font-size:8px}
.hero{min-height:860px;padding:0}
.hero-visual{height:860px}
.hero-copy{left:6%;right:6%;top:42%;max-width:none;padding:22px 18px;transform:translateY(-50%);background:linear-gradient(90deg,rgba(0,0,0,.84),rgba(0,0,0,.36),transparent)}
.hero h1{font-size:58px;line-height:.92}
.hero-description{font-size:14px;line-height:1.65;margin-top:22px}
.hero-buttons{margin-top:24px;gap:12px}
.btn{padding:15px 18px}
.hero-stamp{left:6%;right:auto;bottom:34px;max-width:82%;padding:14px 16px;font-size:12px;line-height:1.45}
.hero-stamp strong{margin-bottom:4px;font-size:17px}
.cuts-section{min-height:430px;padding:105px 8px 45px}
.cut-stage{height:280px}
.cut-slide{width:min(29vw,220px)}
.mission-copy{padding:60px 25px}
.booking{padding:70px 18px}
.booking-form{grid-template-columns:1fr;padding:24px 18px}
.form-group.full,.booking-submit,.booking-success{grid-column:1}
footer{flex-direction:column;text-align:center}
}
</style>
</head>
<body>
<audio id="shopBeat" src="/audio/king_cuts_audio.wav" preload="auto" loop></audio>
<header><a class="logo" href="#home"><div class="logo-crown">♛</div><div class="logo-main">KING’S CUTS</div><div class="logo-sub">BARBERSHOP</div></a><nav><a href="#home">HOME</a><a href="#cuts">THE CUTS</a><a href="#services">SERVICES</a><a href="#mission">OUR STORY</a><a href="#booking">BOOK</a><a href="#contact">CONTACT</a></nav><button id="soundButton" class="sound-button">🔊 CLICK FOR SOUND</button></header>
<section class="hero" id="home"><div class="hero-copy"><div class="eyebrow">CLEAN CUTS • CONFIDENT MEN • STRONGER COMMUNITIES</div><h1>MORE THAN<span class="gold">A HAIRCUT</span></h1><p class="hero-description">Precision barbering for every generation. Clean lines, sharp fades, healthy hair and the confidence that comes with looking your best.</p><div class="hero-buttons"><a class="btn btn-gold" href="#booking">BOOK AN APPOINTMENT →</a><a class="btn btn-dark" href="#cuts">SEE THE CUTS →</a></div></div><div class="hero-visual"><img src="/images/kc_hero.png" alt="King's Cuts barber at work"><div class="hero-stamp"><strong>A HIGHER STANDARD</strong><span>PRECISION • CONFIDENCE • COMMUNITY</span></div></div></section>
<section class="cuts-section" id="cuts"><div class="cuts-header"><small>DIFFERENT STYLES • SAME CONFIDENCE</small><h2>THE CUTS</h2></div><div class="gold-flash" id="goldFlash"></div><div class="cut-stage">
<article class="cut-slide"><img src="/images/image_01.png" alt="King\'s Cuts hairstyle 01"></article>
<article class="cut-slide"><img src="/images/image_02.png" alt="King\'s Cuts hairstyle 02"></article>
<article class="cut-slide"><img src="/images/image_03.png" alt="King\'s Cuts hairstyle 03"></article>
<article class="cut-slide"><img src="/images/image_04.png" alt="King\'s Cuts hairstyle 04"></article>
<article class="cut-slide"><img src="/images/image_05.png" alt="King\'s Cuts hairstyle 05"></article>
<article class="cut-slide"><img src="/images/image_06.png" alt="King\'s Cuts hairstyle 06"></article>
<article class="cut-slide"><img src="/images/image_07.png" alt="King\'s Cuts hairstyle 07"></article>
<article class="cut-slide"><img src="/images/image_08.png" alt="King\'s Cuts hairstyle 08"></article>
</div></section>
<section class="services" id="services"><div class="section-title"><small>KING'S CUTS</small><h2>PREMIUM BARBERING</h2></div><div class="service-grid">
<div class="service"><div class="service-icon">✂</div><h3>HAIRCUTS</h3><p>Precision cuts for all ages</p></div>
<div class="service"><div class="service-icon">♛</div><h3>BEARD CARE</h3><p>Shaping & grooming</p></div>
<div class="service"><div class="service-icon">◈</div><h3>SPECIALTY STYLES</h3><p>Waves • braids • designs</p></div>
<div class="service"><div class="service-icon">★</div><h3>TEEN CUTS</h3><p>Confidence early</p></div>
<div class="service"><div class="service-icon">♚</div><h3>KIDS CUTS</h3><p>A solid foundation</p></div>
<div class="service"><div class="service-icon">◆</div><h3>PREMIUM SERVICE</h3><p>Quality you can trust</p></div>
</div></section>
<section class="mission" id="mission"><div class="mission-image"></div><div class="mission-copy"><small>OUR MISSION</small><h2>A HIGHER <span>STANDARD</span></h2><p>At King's Cuts, we do more than cut hair. We build confidence, strengthen community, and create a place where boys and men of every generation can look good, feel good, and carry themselves differently.</p><p>Precision matters. Presentation matters. Confidence matters.</p></div></section>
<section class="quote"><h2>A FRESH CUT BUILDS <span>A DIFFERENT KIND OF CONFIDENCE.</span></h2></section>

<section class="booking" id="booking">
  <div class="booking-wrap">
    <div class="booking-heading">
      <small>READY FOR YOUR NEXT CUT?</small>
      <h2>BOOK <span>YOUR CUT</span></h2>
      <p>Send your appointment request and KING’S CUTS will contact you to confirm your date and time.</p>
    </div>
    <form class="booking-form" id="bookingForm">
      <div class="form-group">
        <label for="clientName">NAME</label>
        <input id="clientName" name="name" type="text" placeholder="Your name" required>
      </div>
      <div class="form-group">
        <label for="clientPhone">PHONE</label>
        <input id="clientPhone" name="phone" type="tel" placeholder="Your phone number" required>
      </div>
      <div class="form-group">
        <label for="clientEmail">EMAIL</label>
        <input id="clientEmail" name="email" type="email" placeholder="Your email address">
      </div>
      <div class="form-group">
        <label for="service">SERVICE</label>
        <select id="service" name="service" required>
          <option value="" selected disabled>Select a service</option>
          <option>Haircut</option>
          <option>Haircut + Beard</option>
          <option>Beard Care</option>
          <option>Specialty Style</option>
          <option>Teen Cut</option>
          <option>Kids Cut</option>
          <option>Premium Service</option>
        </select>
      </div>
      <div class="form-group">
        <label for="barber">PREFERRED BARBER</label>
        <select id="barber" name="barber">
          <option>No preference</option>
          <option>First Available</option>
          <option>Barber One</option>
          <option>Barber Two</option>
          <option>Barber Three</option>
        </select>
      </div>
      <div class="form-group">
        <label for="appointmentDate">PREFERRED DATE</label>
        <input id="appointmentDate" name="date" type="date" required>
      </div>
      <div class="form-group">
        <label for="appointmentTime">PREFERRED TIME</label>
        <input id="appointmentTime" name="time" type="time" required>
      </div>
      <div class="form-group full">
        <label for="notes">NOTES</label>
        <textarea id="notes" name="notes" placeholder="Tell us anything we should know about your cut."></textarea>
      </div>
      <button class="booking-submit" type="submit">REQUEST APPOINTMENT →</button>
      <div class="booking-success" id="bookingSuccess">
        <strong>APPOINTMENT REQUEST RECEIVED</strong>
        <span>Thank you for choosing KING’S CUTS. We’ll contact you to confirm your appointment.</span>
      </div>
    </form>
  </div>
</section>

<footer id="contact"><div class="footer-brand"><div class="logo-crown">♛</div><div class="logo-main">KING’S CUTS</div><div class="logo-sub">BARBERSHOP</div></div><div>DEMO BARBERSHOP EXPERIENCE</div><div>POWERED BY MAYAKA'AL DIGITAL.</div></footer>
<script>
const beat = document.getElementById("shopBeat");
const soundButton = document.getElementById("soundButton");
beat.volume = .55;

soundButton.addEventListener("click", async () => {
    try {
        if (beat.paused) {
            await beat.play();
            soundButton.innerHTML = "🔊 SOUND ON";
            soundButton.classList.add("active");
        } else {
            beat.pause();
            soundButton.innerHTML = "🔇 SOUND OFF";
            soundButton.classList.remove("active");
        }
    } catch (e) {
        soundButton.innerHTML = "🔊 CLICK FOR SOUND";
    }
});

const slides = [...document.querySelectorAll(".cut-slide")];

const slots = [
    { left: "4%", right: "auto", center: false },
    { left: "50%", right: "auto", center: true },
    { left: "auto", right: "4%", center: false }
];

let imageIndex = 0;
let slotIndex = 0;
let previousCard = null;

const STEP_TIME = 2600;
const CROSSFADE = 1500;

function hiddenTransform(centered) {
    return centered
        ? "translate(-50%, -50%) scale(.96)"
        : "translateY(-50%) scale(.96)";
}

function visibleTransform(centered) {
    return centered
        ? "translate(-50%, -50%) scale(1)"
        : "translateY(-50%) scale(1)";
}

function showNextCard() {
    const card = slides[imageIndex];
    const slot = slots[slotIndex];

    // Prepare the next card invisibly in its fixed LEFT/CENTER/RIGHT position.
    card.style.transition = "none";
    card.style.opacity = "0";
    card.style.left = slot.left;
    card.style.right = slot.right;
    card.style.transform = hiddenTransform(slot.center);

    // Force layout so the fade-in always starts cleanly.
    void card.offsetWidth;

    // Fade the new card in.
    card.style.transition =
        `opacity ${CROSSFADE}ms ease, transform ${CROSSFADE}ms ease`;
    card.style.opacity = "1";
    card.style.transform = visibleTransform(slot.center);

    // At the same time, fade the previous card out.
    if (previousCard && previousCard !== card) {
        const previousCentered = previousCard.style.left === "50%";
        previousCard.style.opacity = "0";
        previousCard.style.transform = hiddenTransform(previousCentered);
    }

    previousCard = card;

    // Always advance in one direction:
    // LEFT -> CENTER -> RIGHT -> LEFT -> CENTER -> RIGHT...
    imageIndex = (imageIndex + 1) % slides.length;
    slotIndex = (slotIndex + 1) % slots.length;
}


const bookingForm = document.getElementById("bookingForm");
const bookingSuccess = document.getElementById("bookingSuccess");

bookingForm.addEventListener("submit", (event) => {
    event.preventDefault();
    bookingSuccess.style.display = "block";
    bookingSuccess.scrollIntoView({behavior:"smooth", block:"nearest"});
    bookingForm.reset();
});

// First image appears immediately, then the procession continues forever.
showNextCard();
setInterval(showNextCard, STEP_TIME);
</script>
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

@app.route("/images/<path:filename>")
def images(filename):
    return send_from_directory(IMAGE_DIR, filename)

@app.route("/audio/<path:filename>")
def audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")), debug=True)
