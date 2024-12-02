# **py_bg_remover** 🌟  
An image background remover written in Python with CI/CD pipeline integration using the **Remove.bg API**. The project includes a simple and user-friendly web frontend built with Flask.

---

## 🚀 **Features**

- Upload images (PNG, JPG, JPEG) via a web interface.
- Automatically remove image backgrounds using the **Remove.bg API**.
- Download the processed image with the background removed.
- Lightweight and simple to use.

---

## 🛠️ **Technologies Used**

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS (for the web interface)  
- **API:** Remove.bg  
- **Others:** Logging, CI/CD pipeline setup  

---

## 💻 **Installation**

1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

2. Add your Remove.bg API Key:
   - Open the `app.py` file.
   - Replace `"SAhGCxs3HGWPSgjm5m8iEVKp"` with your **Remove.bg API key**.

3. Run the Flask app:  
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:  
   ```
   http://localhost:5100
   ```

---

## 🖼️ **How It Works**

1. Open the web application.
2. Upload an image in **PNG, JPG, or JPEG** format.
3. Click the upload button, and the **Remove.bg API** processes the image.
4. Download your background-free image.

---

## ⚡ **Example Usage**

- **Upload Interface:**  
  ![Upload Interface]([https://via.placeholder.com/600x400?text=Upload+Screen](https://postimg.cc/dD8P0g4Q))  

- **Processed Image:**  
  ![Processed Image]([https://via.placeholder.com/600x400?text=Background+Removed](https://postimg.cc/zLL4YQyr))

---

## 🔑 **API Key Instructions**

1. Sign up at [Remove.bg](https://www.remove.bg/) to obtain an API key.
2. Replace the placeholder key in `app.py` with your actual key.
