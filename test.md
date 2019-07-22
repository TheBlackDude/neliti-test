<!-- Compile with: pandoc -s test.md -c pandoc.css -o test.html --metadata pagetitle="Neliti Developer Screening Test" -->

<center>
![Neliti logo](neliti.svg){ width=300px }\ 

# Neliti Developer Screening Test
</center>

Welcome to Neliti! This is a brief screening test so we can get an idea of your knowledge of our stack - Python, Django and ES6. Submit your answer by email to `andrew@neliti.com` in whatever form you think is best.

 - All answers should include a short explanation of your answer alongside the code.
 - If something is ambiguous, make a reasonable assumption, state the assumption in your answer and continue.
 - Use of external libraries is OK - use your judgement.
 - Code efficiency, clarity and style are all important.

**Recommended time: 1 hour**

Good luck!
</center>

# Part 1 - Programming

## Question 1: ES6

Rewrite the following using promises instead of callbacks.

```javascript
const f = (firstName, callback) => {
  setTimeout(() => {
    if (!firstName) return callback(new Error('firstName is required'))
    const fullName = `${firstName} Smith`
    return callback(fullName)
  }, 2000)
}

f('Andrew', console.log)
f(null, console.log)
```

## Question 2: Python

Complete the following function:

```python
def word_frequencies(url):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """
    pass
```

## Question 3: Django
Neliti is primarily a website that hosts academic publications. We record views and downloads of these publications in order to give statistics to our customers. This question is about analysing view and download data to produce some meaningful insights. Here is an excerpt of two models:

```python
class Hit(models.Model):

    PAGEVIEW = 'PV'
    DOWNLOAD = 'DL'
    ACTIONS = (
        (PAGEVIEW, 'Article web page view'),
        (DOWNLOAD, 'Article download'),
    )

    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)
    date = models.DateTimeField(default=django.utils.timezone.now)
    ip_address = models.GenericIPAddressField()
    user_agent = models.ForeignKey('UserAgent', on_delete=models.SET_NULL,
                                   null=True, blank=True)
    action = models.CharField(max_length=2, choices=ACTIONS)


class Publication(models.Model):

    title = models.CharField(max_length=200)
    journal = models.ForeignKey('Journal', on_delete=models.CASCADE)
    # ... remaining fields omitted
```

A `Publication` represents a single journal article on our website ([example](https://www.neliti.com/publications/66008/)). Each time a user accesses a publication, we create a new `Hit` instance. A `Hit` represents either a single view or a single download of a publication. Publications are arranged into collections called journals - a `Journal` is a collection of publications of similar subject matter.

Your task is to write a function `get_journal_statistics()` that returns a `dict` mapping journals to summary statistics:
```python
def get_journal_statistics():
    # Construct summary dict in the form {journal_id -> (total_views, total_downloads)}
    return summary
```

The return value should be a `dict` giving summary statistics for all journals in the form

```
{journal_id -> (total_views, total_downloads)}
```

where

* `journal_id` is the primary key of the journal instance in the `Journal` table
* `total_views` is the total number of `Hit` instances for all publications in that journal and all time with `action == Hit.PAGEVIEW`
* `total_downloads` is the total number of `Hit` instances for all publications in that journal and all time with `action == Hit.DOWNLOAD`.

All journals should be present in the result, and your code should correctly handle cases where there are no hits of the given type.

## Question 4: Algorithms

Given a list of integers and a target integer, write a function that expresses the target integer by inserting `+` and `-` operations between the list items. For example:

```
>>> f([1, 2, 3, 4, 5], 9)
'9 = 1 + 2 - 3 + 4 + 5'
>>> f([2, 5, 60, -5, 3], 69)
'69 = 2 + 5 + 60 - -5 - 3'
>>> f([2, 5, 10], 50)
None
```

- All list items must be used in the solution, they cannot be skipped.
- If there are multiple ways to express the target integer, return any.
- If there is no way to express the target integer, return `None`.
- Your algorithm should be as efficient as possible.

Analyse the running time of your algorithm and discuss whether it is optimal.


# Part 2 - Other questions

Choose one of the following questions and tell us something interesting!

 1. Tell us one thing you are very opinionated about as a developer and why.
 2. Based on your understanding of our company, what do you think our biggest challenge is?
 3. What's one cool feature or idea you'd like to implement if you came to work for us?

# That's it! 🚀


