import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Directory path routing for system media uploads
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set threshold size constraints (16MB maximum per single upload file)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

# Permitted extensions dictionary array 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov', 'avi'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- ACTIVE BOOKING CALENDAR DATABASE ---
# Simply append any date string directly into this list array ('YYYY-MM-DD') 
# to mark it completely unavailable on your live scanner!
BOOKED_DATES = [
    "2026-07-04",  # Example: 4th of July Event
    "2026-10-12",  # Example: Private Event Booking
    "2026-12-31",  # Example: New Year's Booking
]

# Static mock initialization data for live client reviews board
REVIEWS_DATABASE = []

@app.route('/')
def home():
    # Automatically scan eveything inside static/wok folder
    work_dir = os.path.join('static', 'work')
    work_files = os.listdir(work_dir) if os.path.exists(work_dir) else []
        
    return render_template('index.html', status=None, reviews=REVIEWS_DATABASE, work_files=work_files)

@app.route('/check-date', methods=['POST'])
def check_date():
    selected_date = request.form.get('event_date')
    
    if selected_date in BOOKED_DATES:
        status = f"Sorry, {selected_date} is already booked. Please select another date."
    else:
        status = 'available'
    
    # Keep the work files scanning working here too!
    work_dir = os.path.join('static', 'work')
    work_files = os.listdir(work_dir) if os.path.exists(work_dir) else []

    return render_template('index.html', status=status, selected_date=selected_date, reviews=REVIEWS_DATABASE, work_files=work_files)
    
    filename = None
    if file and file.filename != '':
        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return "Error: File format unsupported. Please attach an image or video source format.", 400
        
    # Inject user feedback elements directly into the display dictionary array
    REVIEWS_DATABASE.insert(0, {
        "name": name,
        "text": text,
        "file_path": filename
    })
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Render assigns a port, or we default to 10000
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

