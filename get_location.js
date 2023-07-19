const axios = require('axios');

async function getCurrentLocation() {
  try {
    const response = await axios.get('http://ip-api.com/json/');
    const { lat, lon } = response.data;
    return { latitude: lat, longitude: lon };
  } catch (error) {
    console.error('Failed to fetch geolocation data:', error);
    throw error;
  }
}

getCurrentLocation()
  .then(location => {
    console.log(JSON.stringify(location));
  })
  .catch(error => {
    console.error('Error:', error);
  });
