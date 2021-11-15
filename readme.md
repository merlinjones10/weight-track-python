#Plan
* Create instance of a measurement class
    * get input from user about current weight in kgs
    * attach date to that input

* Add it to DB
    * Create SQLite3 db
    * Make Schema -> Date and Weight
    * Push the measurement to DB

* Get average weight over X amount of days
    * Hard code for 7 for now
    * Create option to get AVG over 7 days
    * Get last 7 measurements, push them to a list and the call avg function on that list
    * Display avg to the user