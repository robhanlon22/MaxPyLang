"""Generate MaxMSP patches for chess board FEN states."""

from __future__ import annotations

import sys
from pathlib import Path

import maxpylang as mp

row_coords = [8, 7, 6, 5, 4, 3, 2, 1]
column_coords = ["a", "b", "c", "d", "e", "f", "g", "h"]
piece_map = {
    "R": "rook",
    "N": "knight",
    "B": "bishop",
    "K": "king",
    "Q": "queen",
    "P": "pawn",
}


def get_synth_info(char: str, row_ind: int, col_ind: int) -> list[str | int]:
    """Return synth metadata for a chess piece."""
    color = "white" if char.isupper() else "black"
    piece_name = piece_map[char.upper()]
    return [piece_name, color, row_ind, col_ind]


def build_patch(synth_info: list[list[str | int]], board_ind: int) -> None:
    """Build and save a MaxMSP patch from a list of synth info."""
    # create empty patch
    patch = mp.MaxPatch()

    # create ezdac
    patch.set_position(500, 900)
    ezdac = patch.place("ezdac~")[0]

    # make all synth objects
    for synth_data in synth_info:
        # get info
        piecename = synth_data[0]
        color = synth_data[1]
        row_ind = synth_data[2]
        col_ind = synth_data[3]

        # make objects w/ specified size
        synth_object = mp.MaxObject(piecename + "-synth", patching_rect=[0, 0, 100, 22])
        color_msg = mp.MaxObject("message " + color, patching_rect=[0, 0, 40, 20])
        col_msg = mp.MaxObject(
            "message " + column_coords[col_ind], patching_rect=[0, 0, 20, 20]
        )
        row_msg = mp.MaxObject(
            "message " + str(row_coords[row_ind]), patching_rect=[0, 0, 20, 20]
        )

        # place objects at custom placements
        patch.place(
            synth_object,
            color_msg,
            col_msg,
            row_msg,
            spacing_type="custom",
            spacing=[
                (col_ind * 120 + 100, row_ind * 100 + 100),
                (col_ind * 120 + 100, row_ind * 100 + 100 - 25),
                (col_ind * 120 + 150, row_ind * 100 + 100 - 25),
                (col_ind * 120 + 180, row_ind * 100 + 100 - 25),
            ],
        )

        # connect objects
        patch.connect(
            (color_msg.outs[0], synth_object.ins[0]),
            (col_msg.outs[0], synth_object.ins[1]),
            (row_msg.outs[0], synth_object.ins[2]),
            (synth_object.outs[0], ezdac.ins[0]),
        )

    # save patch
    patch.save("generated-boards/" + str(board_ind))


def main() -> int:
    """Load FEN strings, build patch files, and return an exit status."""
    # first, read file with FEN strings into a list of split FEN strings
    fens_file = Path("fens.txt")
    fen_strings = [line.split("/") for line in fens_file.read_text().splitlines()]

    # then, process all FEN strings
    for board_ind in range(len(fen_strings)):
        synth_info = []  # save info for synths to make

        # process each row
        for row_ind in range(8):
            row = fen_strings[board_ind][row_ind]

            col_ind = 0  # track column coordinate
            # for each char in each row
            for char in row:
                if char.isnumeric():
                    col_ind += int(char)  # handle numbers in strings
                else:
                    info = get_synth_info(char, row_ind, col_ind)
                    synth_info.append(info)
                    col_ind += 1

        # build patch from synth info
        build_patch(synth_info, board_ind)

    return 0


if __name__ == "__main__":
    sys.exit(main())
