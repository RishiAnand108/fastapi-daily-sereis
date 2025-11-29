param(
    [string]$Repo = "D:\\fastapi-daily-series",
    [string]$Branch = "main",
    [string]$Remote = "origin",
    [switch]$RunTests
)

Set-StrictMode -Version Latest
Write-Output "Starting auto-push for $Repo"

if (-not (Test-Path $Repo)) {
    Write-Error "Repository path '$Repo' does not exist. Aborting."
    exit 1
}

Set-Location $Repo

# Optional: run tests before committing
if ($RunTests) {
    Write-Output "Running tests..."
    if (Get-Command pytest -ErrorAction SilentlyContinue) {
        & pytest
n        if ($LASTEXITCODE -ne 0) {
            Write-Error "Tests failed. Aborting push."
            exit 1
        }
    } else {
        Write-Output "pytest not found; skipping tests."
    }
}

# Stage everything (respect .gitignore)
& git add -A

# Check for changes
$changes = & git status --porcelain
if ([string]::IsNullOrWhiteSpace($changes)) {
    Write-Output "No changes to commit."
    exit 0
}

$timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
$commitMessage = "Auto daily commit $timestamp"

# Commit and push
& git commit -m $commitMessage
if ($LASTEXITCODE -ne 0) {
    Write-Error "git commit failed. Aborting."
    exit 1
}

& git push $Remote $Branch
if ($LASTEXITCODE -ne 0) {
    Write-Error "git push failed. Check authentication and remote settings."
    exit 1
}

Write-Output "Auto-push completed successfully."
