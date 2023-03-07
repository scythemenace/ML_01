
## Supervised Machine Learning
Comprises of 99% of Machine learning applications. It refers to algorithms that learn through input and output mappings, where the outputs have certain kind of label on them.

| Input(x)                         | Output(y)                          |              Application(Label)              |
|----------------------------------|------------------------------------|----------------------------------------------|
| email                            | spam                               | spam filtering                               |
| audio                            | text transcript                    | speech recognition                           |
| English                          | Spanish                            | machine translation                          |
| ad, user info                    | click? (0/1)                       | online advertisement                         |
| image, radar info                | position of other cars             | self-driving cars                            |
| image of phone                   | defect? (0/1)                      | visual inspection                            |

Your goal is to systematically choose the function which gives the best output

There are two types of supervised machine learning:-

### Regression
We could possibly plot a graph and draw a line or a curve or any structure to see the trend and predict other types of data. In this case there could be `infinitely` many possible `outputs` based on how we look at the graph. This type of supervised learning is called **Regression**. They are used to predict numerical outputs, like determining the price of a house.

### Classification
It is different from regression because unlike regression where there are infinitely many outputs based on the function we choose to predict the data, here we have finite outputs(or categories) for an input

For eg. If someone had breast cancer, according to their medical history, we could have two outputs if the tumour is malignant or benign.
Unlike regression, classification doesn’t have a numerical output. Usually many inputs are used to determine the finite outputs.

Suppose we are determining if a tumour is benign or malignant. There are mostly many inputs involved like thickness of tumour clump, uniformity of cell size, uniformity cell shape, age, tumour size, etc to determine the likelihood of a tumour happening.

### Summarising,
the main differences between `Regression` and `Classification` is that in supervised machine learning, there are two main types of algorithms: regression and classification.

Regression is used when the output variable is continuous, meaning that there can be an infinite number of possible outcomes. In regression, the goal is to fit a curve or line to the data to predict future outcomes. For example, you might use regression to predict the price of a house based on its size and location.

Classification, on the other hand, is used when the output variable is categorical, meaning that there are a limited number of possible outcomes. In classification, the goal is to classify new data into one of the predefined categories. For example, you might use classification to predict whether an email is spam or not based on its content.

Both regression and classification are types of supervised learning because the algorithm is trained on labeled data, meaning that the correct answer is provided to the algorithm during training.

## Unsupervised Machine Learning
After supervised learning the most widely used form of machine learning in unsupervised machine learning. Unliked supervised learning where each algorithm was associated with a an output label and all the inputs were grouped together based on those output labels, here we have a **set of inputs** and the algorithm is supposed to **find patterns** or structure among the data i.e. the data is supposed to **figure out** the labels **by itself** and we are not supervising it. 

There are three most common types of unsupervised machine learning algorithms:-
1. ### Clustering
    This is the most common type of unsupervised machine learning algorithms because it takes inputs and groups them into different clusters that is in turn used in many applications.

    **example 1**
    ![news](/googlenews.png "google news image")
    In the above image, currently our news talks about a panda and how it is able to group them is because it has the common keywords panda, twin and zoo. Every day the news is different, but the algorithm is the same as it tries to group the news everyday according to the common keywords.

    **example 2**
    ![data](/data.png "data image")
    In the above table, each row represents a particular gene. Our data will group these types of gene into a specific columns by finding out patterns.
2. ### Anomaly Detection
3. ### Dimensionality reduction