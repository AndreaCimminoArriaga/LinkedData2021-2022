# License analysis
Both datasets belong to the Madrid data portal, so the publisher is the city council of Madrid.
However, the rightsholder is Dirección General de Sostenibilidad y Control Ambiental, to which the responsibility for 
the dataset is attributed.

The data we are going to use for our project has a CC BY 4.0 license, with some additional modification as the 
following ones:
* The date of the last update must be mentioned.
* It may not be indicated, insinuated or suggested that the Community of Madrid and the Madrid City Council participate 
on the project where the data will be used.
* No re-identification of persons process are allowed.

Therefore, we can conclude that **our data are under a CC BY 4.0 license with some extra use conditions**.

Lastly, after a consensus with the whole group, we have decided that, when we publish our data, we will do it under a 
**CC BY 4.0 license** so that anyone who need it can get access to them without problems, regardless of their purpose.

# Resource naming strategy
**The URI our resources will be using is**: "http://www.airqualitypredictor.org/ontology#". We are using a hash namespace
because our ontology is relatively small. Furthermore, the data used will have the following URI:
"http://www.airqualitypredictor.org/data/". Here we need to use a slash namespace because the data we are going to use
is very large and new updates are expected (see 
[Some considerations when choosing a URI namespace](https://www.w3.org/2001/sw/BestPractices/VM/http-examples/2006-01-18/) .

**About the ontology:**

Firstly, we define the **class 'City'** which will be the one that we will link with other ontologies. This class has 
an object property (**hasControlStation**) that connect it with the class 'ControlStation'.
Secondly, we define two more classes, **'ControlStation'** and **'Measurement'**, each one with their own data properties 
and objects properties.
The class 'ControlStation' has two object properties (**isIn**, **hasMeasurement**) that connect this class with other 
clases. 
This class has some data properties:
* **label**:        xsd:string
* **hasAddress**:        xsd:string

From this class we created some subclasses to represent the different types of stations:
* **Suburban**
* **UrbanTraffic**
* **Meteorological**
* **UrbanBackground**

The other class we have defined is 'Measurement', which only have one object property (**isFrom**) that connect this
class with the class 'ControlStation'. Nevertheless, this class has many data properties with their corresponding range 
restrictions:
* **hasMeanValue**:        xsd:float
* **hasMaxValue**:         xsd:float
* **hasMinValue**:         xsd:float
* **hasUnit**:             xsd:string
* **atDate**:          xsd:date
* **atDay**:           xsd:int between 1 and 31
* **atMonth**:         xsd:int between 1 and 12
* **atYear**:          xsd:nonNegativeInteger
* **hasMagnitude**:    xsd:string
* **label**:           xsd:string

From this class we created some subclasses to represent the different types of measurements, such as:
* **Temperature**
* **Precipitation**
* **SO_2** 
* **CO** 
* **NO** 
* **NO_2** 
* **PM2.5**
* **PM10**
* **NOx**
* **O_3**
* **TOL**
* **BEN**
* **EBE**
* **MXY**
* **PXY**
* **CH_4**
