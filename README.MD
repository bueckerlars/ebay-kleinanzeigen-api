# Kleinanzeigen API

## Description
A powerful API interface for Kleinanzeigen.de that enables you to fetch listings and specific data.

## Getting Started

### Want to skip the setup?
Visit [kleinanzeigen-agent.de](https://kleinanzeigen-agent.de/features/developer-api) for our hosted solution with additional features and zero configuration required.

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Playwright

### Installation

1. Clone the repository
```sh
git clone https://github.com/bueckerlars/ebay-kleinanzeigen-api.git
cd ebay-kleinanzeigen-api
```

2. Install dependencies
```sh
pip install -r requirements.txt
playwright install chromium
```

3. Start the API
```sh
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Building and Deploying the Docker Container

You can build and deploy the API using Docker for a consistent and portable environment. Alternatively, you can use the provided `BuildAndDeploy.sh` script for a streamlined process.

#### Prerequisites
- Docker installed on your system.

#### Steps to Build and Deploy

1. **Use the BuildAndDeploy Script**
   Run the following command to build and deploy the Docker container using the provided script:
   ```sh
   ./BuildAndDeploy.sh <image-tag>
   ```
   This script automates the build and deployment process.

2. **Manual Build and Deployment**
   If you prefer manual steps, follow these instructions:

   - **Build the Docker Image**
     Run the following command to build the Docker image:
     ```sh
     docker build -t ebay-kleinanzeigen-api .
     ```

   - **Run the Docker Container**
     Use the following command to start the container:
     ```sh
     docker run -d -p 8000:8000 --name kleinanzeigen-api ebay-kleinanzeigen-api
     ```
     This will run the API on port `8000`.

   - **Access the API**
     Once the container is running, you can access the API at:
     ```
     http://localhost:8000
     ```

   - **Stop the Container**
     To stop the running container, use:
     ```sh
     docker stop kleinanzeigen-api
     ```

   - **Remove the Container**
     If you want to remove the container, run:
     ```sh
     docker rm kleinanzeigen-api
     ```

   - **Remove the Image**
     To delete the Docker image, use:
     ```sh
     docker rmi ebay-kleinanzeigen-api
     ```

### API Endpoints

#### 1. Fetch Listings
**Endpoint:** `GET /inserate`

**Description:** Retrieves a list of listings based on search criteria.

##### Query Parameters:
- **`query`** *(string, optional)*: The search term (e.g., "fahrrad" to search for bicycles).
- **`location`** *(string, optional)*: The location or postal code to narrow the search (e.g., `10178` for Berlin).
- **`radius`** *(integer, optional)*: The search radius in kilometers from the specified location (e.g., `5` for a 5 km radius).
- **`min_price`** *(integer, optional)*: The minimum price in Euros for the listings (e.g., `200` for at least 200 Euros).
- **`max_price`** *(integer, optional)*: The maximum price in Euros for the listings (e.g., `500` for at most 500 Euros).
- **`page_count`** *(integer, optional)*: The number of pages to search or return (e.g., `5` for the first 5 pages, default is 1, max: 20 pages).
- **`category`** *(string, optional)*: The category to filter listings (e.g., `furniture` for furniture-related listings).
- **`min_rooms`** *(integer, optional)*: The minimum number of rooms for the listings (e.g., `2` for at least 2 rooms).
- **`max_rooms`** *(integer, optional)*: The maximum number of rooms for the listings (e.g., `4` for at most 4 rooms).
- **`min_size`** *(integer, optional)*: The minimum size in square meters for the listings (e.g., `50` for at least 50 m²).
- **`max_size`** *(integer, optional)*: The maximum size in square meters for the listings (e.g., `100` for at most 100 m²).
- **`status`** *(string, optional)*: The status of the listings (e.g., `active`, `sold`, `reserved`, or `deleted`).

##### Example Request:
```http
GET /inserate?query=fahrrad&location=10178&radius=5&min_price=200&page_count=5&category=furniture&min_rooms=2&max_rooms=4&min_size=50&max_size=100&status=active
```

#### 2. Fetch Listing Details
**Endpoint:** `GET /inserat/{id}`

**Description:** Retrieves detailed information about a specific listing.

##### Path Parameters:
- **`id`** *(string)*: The unique identifier of the listing to fetch details for.

##### Example Request:
```http
GET /inserat/12345
```


### Documentation

#### API Response Format
All API endpoints return responses in the following JSON format:
```json
{
  "success": true,
  "data": [
    ...
  ]
}
```

API documentation is available at `http://localhost:8000/docs` when running locally.

## License
Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
