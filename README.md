# Super Seek

Team 30's project to integrate GenAI in Seek portal.

# Table of contents.

-[ProjectStructure](#projectStructure)
-[Installation](#installation)
-[Usage](#usage)
-[Contributors](#contributors)

## ProjectStructure

The root directory contains the following folders:

- **Milestone 1**: Identify User Requirements.
- **Milestone 2**: User Interfaces.
- **Milestone 3**: Scheduling and design.
- **Milestone 4**: API Endpoints.
- **Milestone 5**: Test cases, test suite of the project.
- **Milestone 6**: Final submission.

## Installation

1. Clone the git Repo.
2. **Backend**: A Flask based backend that handles the server-side logics.
    - Location: `Milestone 6/Code/Backend/`
    - Key Features: 
        - RestFul API endpoints.
        - Database interactions.
        - Ollama interactions for GenAI.
3. **Frontend**: A Vue.js-based frontend that provides the user interface.
    - Location: `Milestone 6/Code/Frontend/se project`
    - Key Features:
        - Interactive user interfaces.
        - State management.
        - API integration with the backend.

## Usage

### Backend

1. Install all required dependancies.
    ```bash
    pip install -r requirements.txt
2. Navigate to the backend directory.
    ```bash
    cd Milestone 6/Code/Backend
3. Start the flask server.
    ```bash
    python app.py

### Frontend
1. Navigate to frontend directory.
    ```bash
    cd Milestone 6/Code/Frontend/se_project
2. Install the required dependancies.
    ```bash
    npm install
3. Install axios for CORS.
    ```bash
    npm install axios
4. Start the Vue development server.
    ```bash
    npm run serve

5. Open chrome or any other browser and go to
    ```bash
    localhost:8080/
    http://127.0.0.1:8080/

## Contributors

| Name              | Roll Numbers | GitHub Profile                                   | Role or Contribution      |
|-------------------|--------------|--------------------------------------------------|---------------------------|
| Anjali Panchal    | 21F2000411   | [@AnjaliPanchal](https://github.com/anjali088)   | Group leader, Frontend    |
| Sahil Sandhu      | 21F1002317   | [@SahilSandhu](https://github.com/Sandhu16117)   | Frontend, Middleware      |
| Abdul Ahad Rauf   | 21F3002590   | [@AbdulAhad](https://github.com/AbdulAhadRauf)   | Backend                   |
| Sanket Metrewar   | 21F3000961   | [@SanketMetrewar](https://github.com/SanketM05)  | Backend, Research         |
| Aman Verma        | 21F1006376   | [@AmanVerma](https://github.com/amanverma6376)   | Documentation, Research   |
| Neon Thapa        | 21F1000706   | [@NeonThapa](https://github.com/NeonThapa)       | Documentation, Research   |
| Pratham Sharma    | 21F1006197   | [@PrathamSharma](https://github.com/pratham1-s)  | Backend,Project Management|
| Leo Tom           | 21F1005835   | [@LeoTom](https://github.com/select-case)        | Documentation             |
