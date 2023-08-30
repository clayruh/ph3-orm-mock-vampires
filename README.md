# Phase 3 ORM Mock Challenge - Vampires

For this mock challenge, we'll be working with a domain for tracking vampires
and the castles they inhabit.

We have two models: `Vampire` which shows the vampires who live in a `Castle`.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- lists and list Methods
- SQL queries
- ORM methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Only one of the tables, `castles` has been created so far. Additionally the `Castle`
class already has its required functionality and you won't have to build
additional methods for it.

Build out all of the methods listed in the deliverables for `Vampire`. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects. There are no formal tests to run with this code so be
sure to test it in the `debug.py` often.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

- `Vampire classmethod create_table()`
  - Creates a `vampires` table with these columns: id (INTEGER), name (TEXT),
  year_born (INTEGER), castle_id (INTEGER)
- `Vampire __init__(name, year_born, castle_id, id=None)`
  - `Vampire` is initialized with a name (string) and an year_born (integer)
  - When initialized an Vampire should have an id of None
  - Assume that Vampires will always be initialized with the proper data types
- `Vampire __repr__()`
  - Returns the Vampire instance in the format below:
  - `Vampire(id={id} name={name}, year_born={year_born}, castle_id={castle_id})`
- `Vampire property year_born()`
  - Returns the `Vampire`'s year_born
  - The year_born must be an integer between `1431` and `2002`
    - We've chosen 1431 because that's when Vlad Dracula was born and 2002 means a vampire is of drinking age

### SQL Methods

- `Vampire create()`
  - Creates a Vampire in the database with the instance's attributes
- `Vampire update()`
  - Updates a Vampire in the database based on the instance's attributes
- `Vampire classmethod query_all()`
  - Returns a list of Vampire instances based on rows in the database
  - The return value ought to be a list of Vampire instances

### Association Properties

- `Vampire property castle()`
  - Returns the Castle that the Vampire is associated with as an instance
  - If the Vampire is not associated with a Castle returns `None`
  - When setting the castle, if the argument is a `Castle` instance it associates
  the Vampire with the castle
  - The database is already seeded with a pair of castles for testing purposes
    - Castle(id=1, name="Castle Ravenloft")
    - Castle(id=2, name="Bran Castle")

### BONUS Methods

- `Vampire delete()`
  - Deletes the Vampire from the database
  - No return value is necessary for this method
- `Vampire save()`
  - Will either create or update the Vampire in the database depending on
  whether the Vampire has an id
- `Vampire classmethod oldest()`
  - Returns the oldest vampire
- `Castle youngest_resident()`
  - Returns the vampire instance who is youngest for the castle
- `Castle classmethod most_residents()`
  - Returns the castle with the most vampire residents
  - Only returns a single castle if two are tied for most residents
