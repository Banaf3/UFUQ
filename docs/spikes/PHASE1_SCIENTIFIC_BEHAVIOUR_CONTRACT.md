\# Phase 1 Milestone 2C: Scientific Behaviour Contract



\## Status



Draft. This document defines the scientific behaviour required before production

astronomy implementation begins.



It does not authorize catalogue parsing, source-derived artifacts, learner-facing

claims, cultural mappings, or deployment.



\## 1. Purpose



Define the normative astronomy behaviour for converting approved catalogue

astrometry into observer-local directions while keeping scientific calculations,

visibility, scene mapping, and learner scoring separate.



\## 2. Scope



This milestone covers:



\- coordinate states and transformation boundaries;

\- reference frames, epochs, and time scales;

\- proper-motion handling;

\- observer location and datum;

\- Earth-orientation and leap-second data;

\- azimuth and altitude conventions;

\- refraction and horizon behaviour;

\- supported date range;

\- warnings and invalid-input behaviour;

\- scientific error budgeting;

\- independent reference-test requirements.



This milestone does not implement:



\- the I/311 catalogue parser;

\- generated catalogue artifacts;

\- production astronomy code;

\- cultural memberships or routes;

\- the Three.js scene;

\- learner scoring or BKT;

\- persistence or accounts.



\## 3. Normative coordinate pipeline



The intended typed pipeline is:



```text

catalogue astrometry at declared frame and epoch

\-> approved space-motion propagation

\-> celestial intermediate transformation

\-> Earth rotation and terrestrial orientation

\-> observer-dependent geometric horizontal direction

\-> optional refracted direction

\-> separately defined visibility result

\-> separately defined scene mapping

