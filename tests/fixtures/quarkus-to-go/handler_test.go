package migration

import (
	"encoding/json"
	"net/http/httptest"
	"strings"
	"testing"
	"time"
)

func TestHTTPContract(t *testing.T) {
	server := httptest.NewServer(Handler())
	defer server.Close()
	client := server.Client()
	client.Timeout = 5 * time.Second
	for path, status := range map[string]int{"/hello": 200, "/missing": 404, "/failure": 503} {
		t.Run(path, func(t *testing.T) {
			response, err := client.Get(server.URL + path)
			if err != nil {
				t.Fatal(err)
			}
			defer response.Body.Close()
			if response.StatusCode != status {
				t.Fatalf("status = %d, want %d", response.StatusCode, status)
			}
			if path == "/hello" {
				if !strings.HasPrefix(response.Header.Get("Content-Type"), "application/json") {
					t.Fatal("content type")
				}
				var body map[string]string
				if err := json.NewDecoder(response.Body).Decode(&body); err != nil {
					t.Fatal(err)
				}
				if len(body) != 1 || body["message"] != "hello" {
					t.Fatalf("unexpected body: %v", body)
				}
			}
		})
	}
}
