# 🌍 Travel Planner – Django Projektidee

**Travel Planner** ist eine webbasierte Anwendung, mit der Benutzer ihre Reisen planen, verwalten und teilen können. Das Projekt kann schrittweise erweitert werden – ideal für Einsteiger bis Fortgeschrittene.

---

## 🔧 1. Grundgerüst – Benutzer & Reisepläne

**Ziel:** Aufbau eines einfachen Django-Projekts mit User-Management und Trip-Modell.

### Features:
- Django-Projekt mit PostgreSQL-Anbindung
- User-Registration und Login (`django.contrib.auth`)
- Modell `Trip`:
  - `title` (CharField)
  - `start_date`, `end_date` (DateField)
  - `description` (TextField)
- CRUD-Views (Create, Read, Update, Delete) für Trips
- Templates zur Darstellung & Bearbeitung

---

## 🗺️ 2. Ziele & Aktivitäten

**Ziel:** Erweiterung um Reiseziele und Aktivitäten.

### Neue Modelle:
- `Destination`
  - Name, Land, Preis, Beschreibung
- `Activity`
  - z. B. Museen, Restaurants
  - ForeignKey zu `Trip` oder `Destination`

### Umsetzung:
- Nested Formsets oder separate Views zur Aktivitätenerstellung
- Darstellung der Aktivitäten pro Trip

---

## 📍 3. Karten & APIs (mittlerer Schwierigkeitsgrad)

**Ziel:** Integration geographischer Funktionen.

### Features:
- Kartenanzeige mit Leaflet oder Mapbox
- Geocoding-API (z. B. OpenStreetMap/Nominatim)
- Visualisierung der Route und Ziele auf einer Karte

---

## 🚀 4. Erweiterte Features (fortgeschritten)

**Ziel:** Interaktive & kollaborative Anwendung.

### Features:
- Bilder-Upload pro `Destination` oder `Activity`
  - `ImageField`, Media-Konfiguration
- Teilen von Reisen über öffentliche URLs
- Optional: Export als PDF
- Kollaboratives Bearbeiten:
  - Einladung weiterer Nutzer mit Rollen (z. B. Mitreisende)

---

## 🧪 5. Extras (Expert Level)

**Ziel:** Professionelle Tools und Skalierbarkeit.

### Erweiterungen:
- Testabdeckung mit `pytest`, `factory_boy`
- Asynchrone Tasks mit `Celery`
  - z. B. automatische E-Mails oder API-Abfragen
- Caching & Performanceoptimierung
- Deployment mit Docker / Heroku / Railway

---

## 🧰 Tech-Hinweise

- **PostgreSQL** über `settings.py` konfigurieren
- Django-App: `planner` oder `trips`
- Datenbank-Verwaltung über **pgAdmin**
- Authentifizierte Views mit `@login_required`
- Class-Based Views (CBVs) für CRUD
- Optional:
  - REST-API mit **Django REST Framework**
  - Frontend mit **Vue.js** oder **React**

---

## ✅ Lernziele

- Django-Modelle, Views, Templates
- Datenbankmodellierung
- API-Integration & Karten
- User-Management
- Deployment & Testing

---

Viel Erfolg beim Entwickeln deines **Travel Planners**! 🌍✈️
