package main

import (
	"fmt"
	"testing"
)

type Board struct {
	board      [][][]int
	accessible []Tuple
	pieces     map[int]map[int]Piece
}

type Tuple struct {
	x, y int
}

type Piece struct {
	id   int
	data map[string]interface{}
}

func NewBoard(boardData [][][]int) *Board {
	accessible := make([]Tuple, 0)
	pieces := make(map[int]map[int]Piece)

	for y, row := range boardData {
		for x, cell := range row {
			if len(cell) == 0 {
				accessible = append(accessible, Tuple{x: x, y: y})
			}
		}
	}

	return &Board{
		board:      boardData,
		accessible: accessible,
		pieces:     pieces,
	}
}

func (b *Board) AddPiece(id int, data map[string]interface{}) {
	// Add piece to the board's pieces
}

func (b *Board) CurrentLocation(id int) Tuple {
	for y, row := range b.board {
		for x, cell := range row {
			for _, pieceID := range cell {
				if pieceID == id {
					return Tuple{x: x, y: y}
				}
			}
		}
	}
	return Tuple{}
}

func (b *Board) Move(loc Tuple, direction string, magnitude int) Tuple {
	x, y := loc.x, loc.y
	newX, newY := x, y

	switch direction {
	case "n":
		newY -= magnitude
	case "s":
		newY += magnitude
	case "e":
		newX += magnitude
	case "w":
		newX -= magnitude
	case "ne":
		newX += magnitude
		newY -= magnitude
	case "nw":
		newX -= magnitude
		newY -= magnitude
	case "se":
		newX += magnitude
		newY += magnitude
	case "sw":
		newX -= magnitude
		newY += magnitude
	}

	return Tuple{x: newX, y: newY}
}

func (b *Board) ValidMoves(loc Tuple, magnitude int) []Tuple {
	validMoves := make([]Tuple, 0)
	directions := []string{"n", "s", "e", "w", "ne", "nw", "se", "sw"}

	for _, direction := range directions {
		for i := 0; i <= magnitude; i++ {
			moveOption := b.Move(loc, direction, i)
			if b.isAccessible(moveOption) {
				validMoves = append(validMoves, moveOption)
			}
		}
	}

	return validMoves
}

func (b *Board) isAccessible(loc Tuple) bool {
	for _, tuple := range b.accessible {
		if tuple == loc {
			return true
		}
	}
	return false
}

func (b *Board) CommitMove(currentLoc, newLoc Tuple) {
	// Update the board with the move
}

func (b *Board) IdsInCell(loc Tuple) []int {
	return b.board[loc.y][loc.x]
}

func TestBoard(t *testing.T) {
	boardData := [][][]int{
		{{0}, {0}, {0}, {0}, {0}, {}, {}, {}, {0}, {0}, {0}, {0}, {0}},
		{{0}, {0}, {0}, {}, {}, {}, {}, {}, {}, {}, {0}, {0}, {0}},
		{{0}, {0}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {0}, {0}},
		{{0}, {}, {}, {}, {}, {}, {}, {}, {}, {1}, {}, {}, {0}},
		{{0}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {0}},
		{{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}},
		{{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}},
		{{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}},
		{{0}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {0}},
		{{0}, {}, {}, {2}, {}, {}, {}, {}, {}, {}, {}, {}, {0}},
		{{0}, {0}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {0}, {0}},
		{{0}, {0}, {0}, {}, {}, {}, {}, {}, {}, {}, {0}, {0}, {0}},
		{{0}, {0}, {0}, {0}, {0}, {}, {}, {}, {0}, {0}, {0}, {0}, {0}},
	}

	board := NewBoard(boardData)

	loc2 := board.CurrentLocation(2)
	fmt.Println(loc2)

	board.CommitMove(Tuple{x: 3, y: 9}, Tuple{x: 3, y: 10})

	loc2AfterMove := board.CurrentLocation(2)
	fmt.Println(loc2AfterMove)
}
