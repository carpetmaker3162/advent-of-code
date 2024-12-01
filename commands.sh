input() {
    if [[ $# -eq 0 ]]; then
        echo "Usage: input <day number>"
        return 1
    fi
    
    if [[ "${current_dir}" == "/" ]]; then
        echo "Not in aoc folder"
        return 1
    fi

    local filename="input/$1.in"
    nvim "${filename}"
}

day() {
    local current_dir="${PWD}"
    while [[ "${current_dir}" != "/" ]]; do
        if [[ -d "${current_dir}/aoc" ]]; then
            break
        fi
        current_dir="$(dirname "${current_dir}")"
    done

    if [[ "${current_dir}" == "/" ]]; then
        echo "Not in aoc folder"
        return 1
    fi

    local day_number="$1"
    local filename="d${day_number}.py"

    if [[ -e "${filename}" ]]; then
        echo "warning: ${filename} exists"
        nvim "${filename}"
        return 1
    fi

    echo "DAY = ${day_number}\n" > "${filename}"
    cat "template.py" >> "${filename}"

    echo "Day ${day_number} created"
    nvim "${filename}"
}
