<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SkyWings Airlines | Book Flights Worldwide</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f8f9fa;
        }
        
        .hero-overlay {
            background: linear-gradient(to right, rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.3));
        }
        
        .destination-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        .flight-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        
        .mobile-menu {
            transition: all 0.3s ease;
        }
    </style>
</head>
<body class="min-h-screen">
    <!-- Navigation -->
    <nav class="bg-white shadow-lg fixed w-full z-50">
        <div class="max-w-7xl mx-auto px-4">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center">
                    <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/8300322a-98e4-4e35-82ba-40e000c2a456.png" alt="SkyWings Airlines logo" class="h-10">
                </div>
                <div class="hidden md:flex space-x-8">
                    <a href="#" class="text-blue-600 font-medium">Home</a>
                    <a href="#" class="text-gray-700 hover:text-blue-600">Book</a>
                    <a href="#" class="text-gray-700 hover:text-blue-600">Destinations</a>
                    <a href="#" class="text-gray-700 hover:text-blue-600">Deals</a>
                    <a href="#" class="text-gray-700 hover:text-blue-600">Manage</a>
                    <a href="#" class="text-gray-700 hover:text-blue-600">Contact</a>
                </div>
                <div class="hidden md:flex items-center space-x-4">
                    <button class="text-blue-600 font-medium">Sign In</button>
                    <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Join Free</button>
                </div>
                <div class="md:hidden flex items-center">
                    <button id="mobile-menu-button">
                        <i class="fas fa-bars text-gray-700 text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile menu (hidden by default) -->
        <div id="mobile-menu" class="mobile-menu hidden md:hidden bg-white pb-4 px-4">
            <a href="#" class="block py-2 text-blue-600 font-medium">Home</a>
            <a href="#" class="block py-2 text-gray-700">Book</a>
            <a href="#" class="block py-2 text-gray-700">Destinations</a>
            <a href="#" class="block py-2 text-gray-700">Deals</a>
            <a href="#" class="block py-2 text-gray-700">Manage</a>
            <a href="#" class="block py-2 text-gray-700">Contact</a>
            <div class="pt-2 border-t mt-2">
                <button class="w-full py-2 text-blue-600 font-medium">Sign In</button>
                <button class="w-full mt-2 bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Join Free</button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative">
        <div class="h-screen flex items-center">
            <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/79cefc2f-2ff9-478d-8375-c5de70185ef7.png" alt="Modern passenger jet flying through clear blue skies" class="absolute w-full h-full object-cover">
            <div class="hero-overlay absolute w-full h-full"></div>
            <div class="max-w-7xl mx-auto px-4 z-10 text-white w-full">
                <div class="max-w-2xl">
                    <h1 class="text-4xl md:text-5xl font-bold mb-6">Discover the World with SkyWings</h1>
                    <p class="text-xl mb-8">Fly with confidence to over 120 destinations worldwide. Experience premium comfort at affordable prices.</p>
                    <button class="bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700 text-lg font-medium">Book Your Flight</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Flight Search -->
    <section class="max-w-7xl mx-auto px-4 py-12 -mt-20 relative z-10">
        <div class="bg-white rounded-xl shadow-xl p-6 md:p-8">
            <h2 class="text-2xl font-bold mb-6">Find Your Perfect Flight</h2>
            <form id="flight-search-form" class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div>
                    <label class="block text-gray-700 mb-2">From</label>
                    <select id="origin" class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                        <option>Select origin</option>
                        <option>New York (JFK)</option>
                        <option>Los Angeles (LAX)</option>
                        <option>Chicago (ORD)</option>
                        <option>Miami (MIA)</option>
                        <option>London (LHR)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-gray-700 mb-2">To</label>
                    <select id="destination" class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                        <option>Select destination</option>
                        <option>Paris (CDG)</option>
                        <option>Tokyo (HND)</option>
                        <option>Dubai (DXB)</option>
                        <option>Sydney (SYD)</option>
                        <option>Rome (FCO)</option>
                    </select>
                </div>
                <div>
                    <label class="block text-gray-700 mb-2">Departure</label>
                    <input type="date" id="departure-date" class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                </div>
                <div>
                    <label class="block text-gray-700 mb-2">Travelers</label>
                    <select id="travelers" class="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500">
                        <option>1 Adult</option>
                        <option>2 Adults</option>
                        <option>3 Adults</option>
                        <option>4 Adults</option>
                        <option>Family (2+2)</option>
                    </select>
                </div>
                <div class="md:col-span-2 lg:col-span-4 flex justify-center">
                    <button type="submit" class="w-full md:w-auto bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 font-medium">Search Flights</button>
                </div>
            </form>
        </div>
    </section>

    <!-- Available Flights Section -->
    <section id="available-flights" class="max-w-7xl mx-auto px-4 py-16 hidden">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-bold mb-4">Available Flights</h2>
            <p class="text-gray-600 max-w-2xl mx-auto">Here are the flights available based on your search criteria:</p>
        </div>
        <div id="flights-list" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"></div>
    </section>

    <!-- Food Ordering Section -->
    <section id="food-ordering" class="max-w-7xl mx-auto px-4 py-16 hidden">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-bold mb-4">Order Your In-Flight Meal</h2>
            <p class="text-gray-600 max-w-2xl mx-auto">Choose your meal preference for a delightful journey:</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="bg-white rounded-xl shadow-md overflow-hidden">
                <img src="https://via.placeholder.com/300x200" alt="Meal Option 1" class="w-full h-48 object-cover">
                <div class="p-4">
                    <h3 class="font-bold text-xl mb-2">Chicken Pasta</h3>
                    <p class="text-gray-600 mb-4">A delicious chicken pasta with creamy sauce.</p>
                    <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Order Now</button>
                </div>
            </div>
            <div class="bg-white rounded-xl shadow-md overflow-hidden">
                <img src="https://via.placeholder.com/300x200" alt="Meal Option 2" class="w-full h-48 object-cover">
                <div class="p-4">
                    <h3 class="font-bold text-xl mb-2">Vegetarian Salad</h3>
                    <p class="text-gray-600 mb-4">A fresh salad with seasonal vegetables.</p>
                    <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Order Now</button>
                </div>
            </div>
            <div class="bg-white rounded-xl shadow-md overflow-hidden">
                <img src="https://via.placeholder.com/300x200" alt="Meal Option 3" class="w-full h-48 object-cover">
                <div class="p-4">
                    <h3 class="font-bold text-xl mb-2">Beef Steak</h3>
                    <p class="text-gray-600 mb-4">A juicy beef steak served with mashed potatoes.</p>
                    <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Order Now</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Popular Destinations -->
    <section class="max-w-7xl mx-auto px-4 py-16">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-bold mb-4">Popular Destinations</h2>
            <p class="text-gray-600 max-w-2xl mx-auto">Explore our most sought-after locations from around the globe</p>
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="destination-card bg-white rounded-xl shadow-md overflow-hidden transition duration-300">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/67371a3c-068b-44f3-b0a8-57110d6f9ada.png" alt="Eiffel Tower in Paris" class="w-full h-48 object-cover">
                <div class="p-4">
                    <h3 class="font-bold text-xl mb-2">Paris, France</h3>
                    <p class="text-gray-600 mb-4">From $449 roundtrip</p>
                    <button class="text-blue-600 font-medium">View Deals →</button>
                </div>
            </div>
            <div class="destination-card bg-white rounded-xl shadow-md overflow-hidden transition duration-300">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/cc39bcec-7c8f-4c45-b74e-1dd447d1440c.png" alt="Tokyo cityscape" class="w-full h-48 object-cover">
                <div class="p-4">
                    <h3 class="font-bold text-xl mb-2">Tokyo, Japan</h3>
                    <p class="text-gray-600 mb-4">From $899 roundtrip</p>
                    <button class="text-blue-600 font-medium">View Deals →</button>
                </div>
            </div>
            <div class="destination-card bg-white rounded-xl shadow-md overflow-hidden transition duration-300">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/347e3557-77b3-461d-9dde-ad511983c204.png" alt="Maldives" class="w-full h-48 object-cover">
                <div class="p-4">
                    <h3 class="font-bold text-xl mb-2">Malé, Maldives</h3>
                    <p class="text-gray-600 mb-4">From $799 roundtrip</p>
                    <button class="text-blue-600 font-medium">View Deals →</button>
                </div>
            </div>
            <div class="destination-card bg-white rounded-xl shadow-md overflow-hidden transition duration-300">
                <img src="https://storage.googleapis.com/workspace-0f70711f-8b4e-4d94-86f1-2a93ccde5887/image/7db218c8-72a5-4b16-8223-3f915bf6a1d3.png" alt="Rio de Janeiro" class="w-full h-48 object-cover">
                <div class="p-4">
                    <h3 class="font-bold text-xl mb-2">Rio de Janeiro, Brazil</h3>
                    <p class="text-gray-600 mb-4">From $699 roundtrip</p>
                    <button class="text-blue-600 font-medium">View Deals →</button>
                </div>
            </div>
        </div>
    </section>

    <script>
        document.getElementById('flight-search-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const origin = document.getElementById('origin').value;
            const destination = document.getElementById('destination').value;
            const departureDate = document.getElementById('departure-date').value;
            const travelers = document.getElementById('travelers').value;

            // Simulate available flights
            const flights = [
                { flightNumber: 'SW123', from: origin, to: destination, date: departureDate, price: '$499' },
                { flightNumber: 'SW456', from: origin, to: destination, date: departureDate, price: '$599' },
                { flightNumber: 'SW789', from: origin, to: destination, date: departureDate, price: '$699' },
            ];

            // Display available flights
            const flightsList = document.getElementById('flights-list');
            flightsList.innerHTML = ''; // Clear previous results
            flights.forEach(flight => {
                const flightCard = document.createElement('div');
                flightCard.className = 'bg-white rounded-xl shadow-md p-4';
                flightCard.innerHTML = `
                    <h3 class="font-bold text-xl mb-2">Flight ${flight.flightNumber}</h3>
                    <p class="text-gray-600">From: ${flight.from} To: ${flight.to}</p>
                    <p class="text-gray-600">Date: ${flight.date}</p>
                    <p class="text-gray-600">Price: ${flight.price}</p>
                    <button class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">Book Now</button>
                `;
                flightsList.appendChild(flightCard);
            });

            // Show available flights section
            document.getElementById('available-flights').classList.remove('hidden');
            document.getElementById('food-ordering').classList.remove('hidden');
        });
    </script>
</body>
</html>
