-- Keep a log of any SQL queries you execute as you solve the mystery.

-- theft happened at 10.15 a.m.
-- try to know more about the theft and found bakery, interviw transcripts might important
SELECT *
FROM crime_scene_reports
where year = 2021 AND month = 7 AND day = 28
AND street = 'Humphrey Street';

-- find more information throught three interviews
-- the thief withdrew some money at the ATM on Leggett Street
-- within ten minutes of the theft, the thief get into a car in the bakery parking lot and drive away
-- As the thief was leaving the bakery, they called someone who talked to them for less than a minute
-- accomplice bought tomorrow's flight ticket for theft
SELECT transcript
FROM interviews
where year = 2021 AND month = 7 AND day = 28
AND transcript LIKE '%bakery%';

-- find the person who take the earliest flight tomorrow in fiftyville
-- found only one flight take off at 8, others are later than 8
SELECT id
FROM flights
where year = 2021 AND month = 7 AND day = 29
AND origin_airport_id = (
    SELECT id FROM airports where city = 'Fiftyville'
)
ORDER BY hour
LIMIT 1;

-- according to above clues, find the person
-- the thief is Bruce
SELECT name
FROM people
JOIN bank_accounts ON people.id = bank_accounts.person_id
where license_plate IN (
    SELECT license_plate
    FROM bakery_security_logs
    where year = 2021 AND month = 7 AND day = 28
    AND hour = 10 AND minute >15 AND minute < 25
    AND activity = 'exit'
)
AND phone_number IN (
    SELECT caller
    FROM phone_calls
    where year = 2021 AND month = 7 AND day = 28
    AND duration < 60
)
AND account_number IN (
    SELECT account_number
    FROM atm_transactions
    where year = 2021 AND month = 7 AND day = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw'
)
INTERSECT
SELECT name
FROM people
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
where year = 2021 AND month = 7 AND day = 29 AND hour = 8
AND origin_airport_id = (
    SELECT id
    FROM airports
    where city = 'Fiftyville'
);

-- find the city Bruce escaped to
-- aka the first flight's destination
-- Bruce escaped to New York City
SELECT city
FROM airports
JOIN flights ON airports.id = flights.destination_airport_id
where year = 2021 AND month = 7 AND day = 29
AND origin_airport_id = (
    SELECT id
    FROM airports
    where city = 'Fiftyville'
)
ORDER BY hour
LIMIT 1;

-- find the person who talk to Bruce on that day
-- accomplice is Robin
SELECT p1.name
FROM people p1
JOIN phone_calls ON p1.phone_number = phone_calls.receiver
JOIN people p2 ON phone_calls.caller = p2.phone_number
where p2.name = 'Bruce'
AND year = 2021 AND month = 7 AND day = 28
AND duration < 60;