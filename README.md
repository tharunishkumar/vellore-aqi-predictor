# Vellore AQI Predictor - AWS Deployment Guide

This is a simple Flask application that predicts Air Quality Index (AQI) for Vellore using machine learning.

## AWS Deployment Steps

### Prerequisites
1. Install AWS CLI
2. Install EB CLI
3. Have an AWS account with necessary permissions

### Deployment Steps

1. **Install AWS CLI and EB CLI**
```bash
pip install awscli awsebcli
```

2. **Configure AWS Credentials**
```bash
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter your default region (e.g., ap-south-1 for Mumbai)
```

3. **Initialize Elastic Beanstalk Application**
```bash
eb init -p python-3.8 vellore-aqi-predictor --region ap-south-1
```

4. **Create the Environment**
```bash
eb create vellore-aqi-predictor-env
```

5. **Deploy the Application**
```bash
eb deploy
```

6. **Open the Application**
```bash
eb open
```

### Important Files
- `app.py`: Main Flask application
- `train_model.py`: Simple ML model training
- `requirements.txt`: Python dependencies
- `.ebextensions/python.config`: Elastic Beanstalk configuration

### Monitoring and Management
- View logs: `eb logs`
- SSH into instance: `eb ssh`
- Terminate environment: `eb terminate vellore-aqi-predictor-env`

## Local Development
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Train the model:
```bash
python train_model.py
```

3. Run the application:
```bash
python app.py
```

## Notes
- The application uses a simplified ML model for demonstration purposes
- Deployed on t2.micro instance to minimize costs
- Uses Elastic Beanstalk for easy deployment and management
