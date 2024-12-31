(ns morfina.core
    (:require
      [reagent.core :as rg]
      [reagent.dom :as rd]))

;; -------------------------
;; Views

(defn navbar []
  [:div.navbar__container
   [:div.nav-bar__content
    [:div.nav-button__logo-text-container
     [:span.nav-button__text "Morfina Project"]]]])


(defn home-page []
  [:<>
   [navbar]
   [:h1 "Welcome to Morfina"]
   [:div
    [:h2 "Draw cards"]
    [:button "Draw!"]]])

;; -------------------------
;; Initialize app

;; start is called by init and after code reloading finishes
(defn ^:dev/after-load start []
  (rd/render [home-page] (js/document.getElementById "app")))

(defn ^:export init! []
  ;; init is called ONCE when the page loads
  ;; this is called in the index.html and must be exported
  ;; so it is available even in :advanced release builds
  (js/console.log "init")
  ;;(rf/dispatch-sync [::events/initialize-app])
  (start))

;; this is called before any code is reloaded
(defn ^:dev/before-load stop []
  (js/console.log "stop"))
