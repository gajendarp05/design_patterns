package main

import "fmt"

type IBooking interface {
	setName(name string)
	getName() string
}

type Booking struct {
	name string
}

func (b *Booking) setName(name string) {
	b.name = name
}

func (b *Booking) getName() string {
	return b.name
}

type Movies struct {
	Booking
}

type LiveShows struct {
	Booking
}

func newMovies() IBooking {
	return &Movies{
		Booking{
			name: "Charlie",
		},
	}
}

func newLiveShows() IBooking {
	return &LiveShows{
		Booking{
			name: "Comedy",
		},
	}
}

/* If there was no factory method, client code needs to know the details of newMovies() and newLiveShows() to create instances

func main() {
	movies := newMovies()
	log.Println(movies.getName())
	movies.setName("Terminator")
	log.Println(movies.getName())

	liveshows := newLiveShows()
	log.Println(liveshows.getName())
}

*/

// Create a factory method
func getBooking(bookType string) IBooking {
	if bookType == "movies" {
		return newMovies()
	}
	if bookType == "liveshows" {
		return newLiveShows()
	}
	return nil
}

func main() {
	b1 := getBooking("movies")
	fmt.Println(b1.getName())

	b2 := getBooking("liveshows")
	fmt.Println(b2.getName())
}
