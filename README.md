# Medical-Cost-Personal

#### we are trying to predict annual health insurance cost charged to a customer by a insurance company based on the major factors like: bmi(body mass index) + age + smoking + children + region they live in

#### people who are benifited are 
### customer -> insurance company pays some amount (can be full or any amount) to the hospital when the user is admitted as a patient
### insurance company -> they set price based on the risk


## THE BMI (BODY MASS INDEX) MEANS HOW MUCH YOUR BODY WEIGHT SHOULD BE ACCORDING TO YOUR HEIGHT

##### SO WE NEED A PERSON BODY WEIGHT IN (KG) AND BODY HEIGHT (IN SQUARE OF METER)

## FORMULA: BMI = BODY WEIGHT(KG) / (HEIGHT (m))^2

#### STEPS TO CONVERT:

#### STEP 1: CONVERT BODY HEIGHT (IN FOOT INTO INCHES): FORMULA = Foot * 12
#### STEP 2: CONVERT BODY WEIGHT (INCHES INTO METER): FORMULA: Inches * 0.0254(not precise value but will do the work done)
#### STEP 3: SQUARE THE METER: (m)^2
#### STEP 4: APPLY BMI FORMULA = BODY HEIGHT (KG) / (BODY WEIGHT(m)^2)

## EXAMPLE: 57 KG OF PERSON / 2.8103 [ (m)^2 ] = 20.28

| BMI Range      | Category      |
| -------------- | ------------- |
| Less than 18.5 | Underweight   |
| 18.5 – 24.9    | Normal weight |
| 25 – 29.9      | Overweight    |
| 30 or more     | Obese         |

