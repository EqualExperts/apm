package migration

import (
	"encoding/json"
	"errors"
	"net/http"
)

func greeting(fail bool) (map[string]string, error) {
	if fail {
		return nil, errors.New("unavailable")
	}
	return map[string]string{"message": "hello"}, nil
}

func Handler() http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet || (r.URL.Path != "/hello" && r.URL.Path != "/failure") {
			http.NotFound(w, r)
			return
		}
		payload, err := greeting(r.URL.Path == "/failure")
		if err != nil {
			http.Error(w, "unavailable", http.StatusServiceUnavailable)
			return
		}
		body, err := json.Marshal(payload)
		if err != nil {
			http.Error(w, "encoding failed", http.StatusInternalServerError)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write(body)
	})
}
