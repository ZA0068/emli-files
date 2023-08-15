<?php
// Specify the path to the security log file
$log_file = '/home/EMLI_TEAM_24/log/securitylogging.log';

// Check if the file exists
if (!file_exists($log_file)) {
    die("Error: Log file '$log_file' does not exist.");
}

// Check if the file is readable
if (!is_readable($log_file)) {
    die("Error: Log file '$log_file' is not readable.");
}

// Read the log file into an array, one line per element
$log = file($log_file);

// Check if the file was read successfully
if ($log === false) {
    die("Error: Failed to read log file '$log_file'.");
}

// Only take the last 10 lines of the log (as there are 10 lines per log entry)
$log = array_slice($log, -5);

// Initialize an empty array to hold the log data
$data = array();

// Loop through the log lines
foreach ($log as $line) {
    // Split the line into key/value pairs
    $parts = explode(':', $line, 2);
    if (count($parts) == 2) {
        // Remove any excess whitespace
        $key = trim($parts[0]);
        $value = trim($parts[1]);
        
        // Add the data to the array
        $data[$key] = $value;
    }
}

// Now you can output the data in a table with a red theme
echo '<style>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

tr:nth-child(even){background-color: #ffe6e6} /* Light red for even rows */

th {
  background-color: #ff3333;  /* Red color for header */
  color: white;
}
</style>';

echo '<table>';
foreach ($data as $key => $value) {
    echo '<tr>';
    echo '<th>' . htmlspecialchars($key) . '</th>';
    echo '<td>' . htmlspecialchars($value) . '</td>';
    echo '</tr>';
}
echo '</table>';
?>