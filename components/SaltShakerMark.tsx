export function SaltShakerMark({ className }: { className?: string }) {
  return (
    <svg
      viewBox="0 0 32 32"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      aria-hidden="true"
    >
      <g transform="rotate(-22 13 16)">
        {/* Cap */}
        <rect
          x="8.5"
          y="4"
          width="9"
          height="3.2"
          rx="0.8"
          fill="currentColor"
          opacity="0.95"
        />
        {/* Cap holes */}
        <circle cx="11" cy="5.6" r="0.55" className="fill-iron" />
        <circle cx="13" cy="5.6" r="0.55" className="fill-iron" />
        <circle cx="15" cy="5.6" r="0.55" className="fill-iron" />
        {/* Neck */}
        <path d="M9.8 7.2h8.4v1.4H9.8z" fill="currentColor" opacity="0.7" />
        {/* Body */}
        <path
          d="M9.2 8.6h9.6l-.7 13.6c-.1 1.5-1.4 2.6-2.9 2.6h-2.4c-1.5 0-2.8-1.1-2.9-2.6L9.2 8.6Z"
          fill="currentColor"
          opacity="0.88"
        />
      </g>

      {/* Salt grains */}
      <g className="salt-sprinkle">
        <circle cx="20.5" cy="8.2" r="0.7" fill="currentColor" opacity="0.8" />
        <circle
          cx="22.8"
          cy="10.6"
          r="0.55"
          fill="currentColor"
          opacity="0.65"
        />
        <circle
          cx="21.4"
          cy="12.8"
          r="0.45"
          fill="currentColor"
          opacity="0.5"
        />
        <circle
          cx="24.2"
          cy="13.5"
          r="0.5"
          fill="currentColor"
          opacity="0.55"
        />
        <circle
          cx="22.6"
          cy="15.8"
          r="0.4"
          fill="currentColor"
          opacity="0.4"
        />
        <circle cx="25" cy="16.6" r="0.35" fill="currentColor" opacity="0.3" />
      </g>
    </svg>
  );
}
