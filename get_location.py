import subprocess
import json

def get_current_location():
    # Jalankan skrip JavaScript menggunakan Node.js dan tangkap outputnya
    output = subprocess.check_output(['node', 'get_location.js']).decode('utf-8').strip()

    # Parse output konsol JavaScript menjadi objek Python
    location = json.loads(output)

    # Dapatkan nilai latitude dan longitude
    latitude = location['latitude']
    longitude = location['longitude']

    return latitude, longitude
