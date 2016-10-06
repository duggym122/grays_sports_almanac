# Grays Sports Almanac

## Project Information

### Package Information
|         Package        |                                                                  Description                                                                     | Version |
| :--------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: | :-----: |
| grays\_sports\_almanac | This package provides a database schema for sports data and the machine learning tooling available to use the database to predict future games.  |  v0.0.1 |

### Status

| Travis-CI | Coveralls |
| :-------: | :-------: |
| [![Build Status](https://travis-ci.org/duggym122/grays_sports_almanac.svg?branch=master)](https://travis-ci.org/duggym122/grays_sports_almanac) | [![Coverage Status](https://coveralls.io/repos/github/duggym122/grays_sports_almanac/badge.svg?branch=master)](https://coveralls.io/github/duggym122/grays_sports_almanac?branch=master) |

### Issue Tracking
[JIRA]

## Roadmap
* Generic sports database including the following entities:
  * League
  * Team
  * Game
  * Championship
* Sport-Specific Predictors
  * Algorithms To Test Out:
    * k-Nearest Neighbour (kNN)
    * Learning Vector Quantization (LVQ)
    * Self-Organizing Map (SOM)
    * Locally Weighted Learning (LWL)
    * Apriori
    * Eclat
* Sport data API integration
  * TBD

**NOTE: This project is still in very early development, so it is subject to some very drastic, and potentially backwards-incompatible changes during the process.**

## Tools

### Psycopg
This is the recommended postgres library for Python. Install using the command ``pip install psycopg2``

### TensorFlow
This is the selected machine learning library

## Installation

### TensorFlow
Follow the [https://www.tensorflow.org/versions/r0.11/get_started/os_setup.html#pip-installation instructions online.]

## Running The Project

Run "python setup.py nosetests" to build and test

## GNU Affero General Public License v3.0

The Conference Room Manager will allow users to manage office locations, conference rooms, and reservations.
Copyright (C) 2016  Douglas Melvin

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.
