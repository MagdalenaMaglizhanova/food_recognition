import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Food Calorie Detector", layout="centered")
st.title("🍎 Food & Calorie Classifier")
st.write("Покажи плод/храна пред камерата и ще ти каже какво е и колко калории има.")

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Fruit Classifier</title>
  <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.3.1/dist/tf.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@0.8.3/dist/teachablemachine-image.min.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background: #f0f0f0;
      padding: 20px;
    }
    video {
      border: 4px solid #333;
      border-radius: 10px;
      margin-bottom: 20px;
    }
    #result {
      font-size: 1.5em;
      margin-top: 10px;
      background: #fff;
      display: inline-block;
      padding: 10px 20px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
  </style>
</head>
<body>
  <h1>🍎 Food & Fruit Classifier</h1>
  <video id="webcam" autoplay playsinline width="224" height="224"></video>
  <div id="result">Loading...</div>

  <script type="text/javascript">
    const URL = "./"; 
    let model, webcam;

    const calorieTable = {
      "Egg": 155,
      "Tomato": 18,
      "Onion": 40,
      "Banana": 89,
      "Orange": 47,
      "Carrot": 41,
      "Cucumber": 16,
      "Pepper": 20,
      "Apricot": 48,
      "Eggplant": 25,
      "Apple": 52,
      "Lukanka": 450
    };

    async function init() {
      model = await tmImage.load(URL + "model.json", URL + "metadata.json");
      webcam = new tmImage.Webcam(224, 224, true);
      await webcam.setup();
      await webcam.play();
      window.requestAnimationFrame(loop);
      document.getElementById("webcam").appendChild(webcam.canvas);
    }

    async function loop() {
      webcam.update();
      await predict();
      window.requestAnimationFrame(loop);
    }

    async function predict() {
      const prediction = await model.predict(webcam.canvas);
      const top = prediction.sort((a, b) => b.probability - a.probability)[0];
      const label = top.className;
      const calories = calorieTable[label] || "?";

      document.getElementById("result").innerHTML = `
        <strong>${label}</strong><br>
        🥗 ~${calories} kcal / 100g
      `;
    }

    init();
  </script>
</body>
</html>
"""

components.html(html_code, height=600)
